import cv2
img = cv2.imread("image.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

sx = cv2.convertScaleAbs(sx)
sy = cv2.convertScaleAbs(sy)

sobel = cv2.addWeighted(sx, 0.5, sy, 0.5, 0)

cv2.imshow("Original Image", img)
cv2.imshow("Sobel X", sx)
cv2.imshow("Sobel Y", sy)
cv2.imshow("Sobel Combined", sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()
