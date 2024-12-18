import cv2
import matplotlib.pyplot as plt
# Reading image
img = cv2.imread("C:/Users/akalf/Documents/Lenna.png")

# Convert BGR to RGB 
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Median Filer for kernel sizes 3, 5 & 7 
m3 = cv2.medianBlur(img1, 3)
m5 = cv2.medianBlur(img1, 5)
m7 = cv2.medianBlur(img1, 7)

# Plot the images using matplotlib
plt.subplot(221), plt.imshow(img1), plt.title("Original Image:"), plt.axis("off")
plt.subplot(222), plt.imshow(m3), plt.title("Median Blur(k = 3 * 3):"), plt.axis("off")
plt.subplot(223), plt.imshow(m5), plt.title("Median Blur(k = 5 * 5):"), plt.axis("off")
plt.subplot(224), plt.imshow(m7), plt.title("Median Blur(k = 7 * 7):"), plt.axis("off")

cv2.waitKey(0)
cv2.destroyAllWindows()
