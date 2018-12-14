import cv2
import glob

images=glob.glob("*.jpg")

for image in images:
    img= cv2.imread(image,1)
    img2 = cv2.resize(img,(100,100))
    cv2.imshow("resized_image",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_image"+image,img2)

