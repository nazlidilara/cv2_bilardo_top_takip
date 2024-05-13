import cv2
import numpy as np

def apply_gaussian_blur(frame, kernel_size=3):
    return cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)

def convert_to_hsv(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

def filter_red_color(hsv_frame):
    lower_red1 = np.array([10, 150, 150])
    upper_red1 = np.array([15, 255, 255])
    lower_red2 = np.array([156, 150, 147])
    upper_red2 = np.array([189, 260, 260])

    mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
    return cv2.bitwise_or(mask1, mask2)

def apply_morphological_ops(mask):
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)
    mask = cv2.erode(mask, kernel, iterations=1)
    return mask

def find_and_draw_contours(mask, frame):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50:  # Alan filtresini değiştirdim
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            if radius > 5:  # Radius filtresi eklendi
                center = (int(x), int(y))
                cv2.circle(frame, center, int(radius), (0, 255, 0), 2)
                cv2.putText(frame, "Kirmizi", center, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        blurred_frame = apply_gaussian_blur(frame)
        hsv_frame = convert_to_hsv(blurred_frame)
        red_mask = filter_red_color(hsv_frame)
        clean_mask = apply_morphological_ops(red_mask)
        find_and_draw_contours(clean_mask, frame)

        cv2.imshow('Kirmizi Toplar', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
process_video("C:\\Users\\Lenovo\\Desktop\\vid_1.avi")

