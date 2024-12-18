import cv2
import matplotlib.pyplot as plt
# Reading image
img = cv2.imread("C:/Users/akalf/Documents/Lenna.png")

# Convert BGR to RGB 
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Bilateral Filter
b5 = cv2.bilateralFilter(img1, 5, 75, 75)
b15 = cv2.bilateralFilter(img1, 15, 100, 100)

# Display the images using plotting
plt.subplot(131), plt.imshow(img1), plt.title("Original Image:"), plt.axis("off")
plt.subplot(132), plt.imshow(b5), plt.title("Bilateral Filter(k = 5 * 5):"), plt.axis("off")
plt.subplot(133), plt.imshow(b15), plt.title("Bilateral Filter(k = 15 * 15):"), plt.axis("off")

cv2.waitKey(0)
cv2.destroyAllWindows()
