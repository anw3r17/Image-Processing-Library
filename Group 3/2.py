import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading image
img = cv2.imread("C:/Users/akalf/Documents/abcd.jpg")

# Convert to GRAYSCALE
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Binary Thresholding
ret, t = cv2.threshold(img1, 70, 255, cv2.THRESH_BINARY)

# Make a Kernel filter for multiple iterations
k = np.ones((5, 5), np.uint8)
print(k)

# Applying erosion
d1 = cv2.dilate(t, k, iterations = 1)
d2 = cv2.dilate(t, k, iterations = 2)
d3 = cv2.dilate(t, k, iterations = 3)

# Displaying the images using plotting
plt.subplot(231), plt.imshow(img1), plt.title("Original Image:"), plt.axis("off")
plt.subplot(232), plt.imshow(t, cmap = "gray"), plt.title("Threshold Image:"), plt.axis("off")
plt.subplot(233), plt.imshow(d1, cmap = "gray"), plt.title("Dilation i = 1:"), plt.axis("off")
plt.subplot(234), plt.imshow(d2, cmap = "gray"), plt.title("Dilation i = 2:"), plt.axis("off")
plt.subplot(235), plt.imshow(d3, cmap = "gray"), plt.title("Dilation i = 3:"), plt.axis("off")
plt.savefig("C:/Users/akalf/Documents/updated(d).png", format = "png", dpi = 1200)

