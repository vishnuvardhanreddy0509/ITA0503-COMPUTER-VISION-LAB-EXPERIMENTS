import cv2

# Read the image
image = cv2.imread("im3.jpg")   # Replace with your image filename

# Check if image is loaded
if image is None:
    print("Error: Could not load image.")
    exit()

# Display original image
cv2.imshow("Original Image", image)

# Get original dimensions
height, width = image.shape[:2]

print("Original Image Size:")
print("Width:", width)
print("Height:", height)

# -------------------------------
# Resize image to bigger size
# -------------------------------

# Increase size by 2 times
bigger_image = cv2.resize(
    image,
    (width * 1, height * 1),
    interpolation=cv2.INTER_LINEAR
)

# Display bigger image
cv2.imshow("Bigger Image", bigger_image)


# -------------------------------
# Resize image to smaller size
# -------------------------------

# Reduce size by half
smaller_image = cv2.resize(
    image,
    (width // 2, height // 2),
    interpolation=cv2.INTER_AREA
)

# Display smaller image
cv2.imshow("Smaller Image", smaller_image)


# Save resized images
cv2.imwrite("bigger_image.jpg", bigger_image)
cv2.imwrite("smaller_image.jpg", smaller_image)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
