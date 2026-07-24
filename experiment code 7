import cv2

# Open the video file
video = cv2.VideoCapture("video2.mp4")   # Replace with your video file

# Check if the video opened successfully
if not video.isOpened():
    print("Error: Could not open video.")
    exit()

print("Press:")
print("n - Normal Speed")
print("s - Slow Motion")
print("f - Fast Motion")
print("q - Quit")

# Initial delay for normal speed
delay = 30

while True:
    ret, frame = video.read()

    if not ret:
        print("End of video.")
        break

    # Display the video
    cv2.imshow("Video Processing", frame)

    # Wait according to selected speed
    key = cv2.waitKey(delay) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('n'):
        delay = 30          # Normal speed
    elif key == ord('s'):
        delay = 200         # Slow motion
    elif key == ord('f'):
        delay = 10          # Fast motion

# Release resources
video.release()
cv2.destroyAllWindows()
