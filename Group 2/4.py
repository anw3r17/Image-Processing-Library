import cv2
import matplotlib.pyplot as plt
# Reading image
img = cv2.imread("C:/Users/akalf/Documents/Lenna.png")

# Convert BGR to RGB 
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Box Blur / Mean Filter
b3 = cv2.blur(img1, (3, 3))
b5 = cv2.blur(img1, (5, 5))
b10 = cv2.blur(img1, (10, 10))

# Display all the Images using ploting
plt.subplot(221), plt.imshow(img1), plt.title("Original Image:"), plt.axis("off")
plt.subplot(222), plt.imshow(b3), plt.title("Box Blur (k = 3 * 3)"), plt.axis("off")
plt.subplot(223), plt.imshow(b5), plt.title("Box Blur (k = 5 * 5)"), plt.axis("off")
plt.subplot(224), plt.imshow(b10), plt.title("Box Blur (k = 10 * 10)"), plt.axis("off")

cv2.waitKey(0)
cv2.destroyAllWindows()

