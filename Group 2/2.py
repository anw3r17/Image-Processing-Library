import cv2
import matplotlib.pyplot as plt
# Reading image
img = cv2.imread("C:/Users/akalf/Documents/Lenna.png")

# Convert BGR to RGB 
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Applying Gaussian Filter
g5 = cv2.GaussianBlur(img1, (5, 5), 5)
g15 = cv2.GaussianBlur(img1, (15, 15), 5)

# Plot and Display all the images 
plt.subplot(131), plt.imshow(img1), plt.title("Original Image:"), plt.axis("off")
plt.subplot(132), plt.imshow(g5), plt.title("Gaussian Blur (k = 5 * 5)"), plt.axis("off")
plt.subplot(133), plt.imshow(g15), plt.title("Gaussian Blur (k = 15 * 15)"), plt.axis("off")

cv2.waitKey(0)
cv2.destroyAllWindows()