import cv2
import numpy as np

def get_roi(edges):
    h, w = edges.shape

    polygon = np.array([[(0, h), (w // 2-100, int(h * 0.7)), (w // 2 + 100, int(h * 0.7)),(w, h) ]])
    mask = np.zeros_like(edges)
    cv2.fillPoly(mask, polygon, 255)

    return cv2.bitwise_and(edges, mask)

def detect_lanes(frame, lines):
    if lines is None:
        return []

    left, right = [], []

    for line in lines:
        x1, y1, x2, y2 = line[0]

        if x1 == x2:
            continue

        slope, intercept = np.polyfit( (x1, x2), (y1, y2),   1 )

        if slope < -0.5:
            left.append((slope, intercept))
        elif slope > 0.5:
            right.append((slope, intercept))

    lanes = []
    h = frame.shape[0]
    y1 = h
    y2 = int(h * 0.7)

    for group in [left, right]:
        if group:
            slope, intercept = np.mean(group, axis=0)

            x1 = int((y1 - intercept) / slope)
            x2 = int((y2 - intercept) / slope)

            lanes.append([x1, y1, x2, y2])



    return lanes


def draw_lanes(frame, lanes):
    overlay = np.zeros_like(frame)

    if len(lanes) == 2:
        left, right = lanes

        cv2.fillPoly(overlay,[np.array([ (left[0], left[1]),(left[2], left[3]),(right[2], right[3]),(right[0], right[1]) ])], (0, 255, 0))

        for lane in lanes:
            cv2.line(overlay,(lane[0], lane[1]),(lane[2], lane[3]),(255, 255, 255),4)
    return cv2.addWeighted(frame, 1, overlay, 0.4, 0)


def process(frame):
    frame = cv2.resize(frame, (640, 480))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blur, 50, 150)
    roi = get_roi(edges)


    lines = cv2.HoughLinesP(roi,2, np.pi / 180,50,minLineLength=40, maxLineGap=100 )
    lanes = detect_lanes(frame, lines)
    return draw_lanes(frame, lanes)


cap = cv2.VideoCapture('video4.web')

while True:
    success, frame = cap.read()

    if not success:
        break
    process(frame)
    cv2.imshow("Track videO", process(frame))
    resut = cv2.resize(frame, (640, 480))
    cv2.imshow("Normal video", resut)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


