import cv2

image = cv2.imread("C:/programming/deep_learning/OpenCV/angry.jpg", cv2.IMREAD_ANYCOLOR)
cv2.imshow("angry", image)
cv2.waitKey()
cv2.destroyAllWindows()