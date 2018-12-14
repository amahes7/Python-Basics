import cv2, time

video=cv2.VideoCapture(0)

while True:
    check,frame = video.read()
    print(frame)
    print(check)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1)

    if key ==ord('e'):
        break
    
video.release()
cv2.destroyAllWindows



