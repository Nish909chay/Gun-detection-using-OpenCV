import numpy as np
import cv2
import imutils
import datetime

gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)

firstFrame = None
gun_exists = False

while True:
    ret, frame = camera.read()
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))
    
    gun_exists = len(gun) > 0
    
    for (x, y, w, h) in gun:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    if firstFrame is None:
        firstFrame = gray
        continue
    
    # Overlay text on the frame
    text = "Gun Detected" if gun_exists else "No Gun Detected"
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow("Feed", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

