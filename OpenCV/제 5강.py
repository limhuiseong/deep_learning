import cv2
src = cv2.imread("C:/programming/deep_learning/OpenCV/angry.jpg", cv2.IMREAD_COLOR)
dst = cv2.flip(src, 0)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()