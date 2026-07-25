import cv2

# Read the image
image = cv2.imread("im.jpg")   # Replace with your image filename

# Check if image is loaded
if image is None:
    print("Error: Could not load image.")
    exit()

# Rotate image 90 degrees clockwise
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Display original and rotated images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image 90 Degree Clockwise", rotated_image)

# Save rotated image
cv2.imwrite("rotated_90_clockwise.jpg", rotated_image)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
