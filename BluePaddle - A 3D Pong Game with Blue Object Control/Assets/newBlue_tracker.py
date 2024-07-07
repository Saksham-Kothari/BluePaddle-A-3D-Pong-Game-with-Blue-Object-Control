import numpy as np
import cv2
import socket

# Setup UDP socket
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 22222
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define color ranges for multiple colors
color_ranges = {
    'blue': (np.array([94, 80, 2]), np.array([120, 255, 255])),
    'green': (np.array([25, 52, 72]), np.array([102, 255, 255])),
    'red': (np.array([136, 87, 111]), np.array([180, 255, 255]))
}

# Capture video through webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Apply morphological transformations and color detection
    kernel = np.ones((5, 5), np.uint8)
    for color, (lower, upper) in color_ranges.items():
        mask = cv2.inRange(hsv, lower, upper)
        mask = cv2.dilate(mask, kernel)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        # Find contours and draw bounding boxes
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 300:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, color.capitalize(), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Multiple Color Detection in Real-Time', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
