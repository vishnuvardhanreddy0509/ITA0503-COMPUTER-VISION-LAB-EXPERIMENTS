import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Could not load image '{image_path}'")
        return

    # Define color channels
    color_channels = ('b', 'g', 'r')

    # Create the plot
    plt.figure(figsize=(10, 5))

    # Calculate and plot histogram for each channel
    for i, color in enumerate(color_channels):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=f"{color.upper()} Channel")

    # Customize the plot
    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.xlim([0, 256])
    plt.legend()
    plt.grid(True)

    # Display the histogram
    plt.show()


# Main program
if __name__ == "__main__":
    image_path = "im2.jpg"      # Replace with your image filename
    analyze_histogram(image_path)
