import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("news.jpg")

img_g =cv2.imread("news.jpg",0)

faces=face_cascade.detectMultiScale(img_g,scaleFactor=1.1,minNeighbors=5)

for x,y,w,h in faces:
    img_updated=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)


print(faces)
print(type(faces))
cv2.imshow("face",img_updated)
cv2.waitKey(0)
cv2.destroyAllWindows()
