import cv2
import numpy as np

# Define image dimensions
height = 500  # Height of the image
width = 500   # Width of the image

# Create a white image (all pixel values set to 255)
white_image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Display the image using OpenCV
cv2.imshow('White Image', white_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
