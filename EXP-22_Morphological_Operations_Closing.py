import cv2
import numpy as np

image = cv2.imread("im.jpg", 0)   

if image is None:
    print("Error: Image not found!")
    exit()

kernel = np.ones((5, 5), np.uint8)

closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original Image", image)
cv2.imshow("Closing Image", closing)

cv2.waitKey(0)

cv2.destroyAllWindows()
