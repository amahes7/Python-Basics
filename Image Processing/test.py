import cv2

img = cv2.imread("1.jpeg",0)

img2=cv2.resize(img,(500,500))
cv2.imshow("Random",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("new.jpg",img2)