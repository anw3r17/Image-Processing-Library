import cv2
import matplotlib.pyplot as plt

# Reading image
img = cv2.imread("C:/Users/akalf/Documents/Lenna.png")

# Convert BGR to GRAY
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel Operator
sx1 = cv2.Sobel(img1, cv2.CV_64F, 1, 0, ksize=5)  
sy1 = cv2.Sobel(img1, cv2.CV_64F, 0, 1, ksize=5)  

# Combine Sobel results
sob1 = sx1 + sy1

# Inverse Thresholding
r, t1 = cv2.threshold(sob1, 120, 255, cv2.THRESH_BINARY_INV)

# Denoise the Image
dn = cv2.GaussianBlur(img1, (3, 3), 0)

# Apply Sobel Operator
sx2 = cv2.Sobel(dn, cv2.CV_64F, 1, 0, ksize=5)  
sy2 = cv2.Sobel(dn, cv2.CV_64F, 0, 1, ksize=5)  

# Combine the Sobel Results
sob2 = sx2 + sy2

# Apply Inverse Thresholding
r2, t2 = cv2.threshold(sob2, 120, 255, cv2.THRESH_BINARY_INV)

# Display the Results on 2 grids
plt.subplot2grid((5, 2), (0, 0)), plt.imshow(img1), plt.title("Original Grayscale Image:"), plt.axis("off")
plt.subplot2grid((5, 2), (1, 0)), plt.imshow(sx1, cmap="gray"), plt.title("Sobel x:"), plt.axis("off")
plt.subplot2grid((5, 2), (2, 0)), plt.imshow(sy1, cmap="gray"), plt.title("Sobel y:"), plt.axis("off")
plt.subplot2grid((5, 2), (3, 0)), plt.imshow(sob1, cmap="gray"), plt.title("Sobel Edge Detection:"), plt.axis("off")
plt.subplot2grid((5, 2), (4, 0)), plt.imshow(t1, cmap="gray"), plt.title("After Inverse Thresholding:"), plt.axis("off")

plt.subplot2grid((5, 2), (0, 1)), plt.imshow(sx2, cmap="gray"), plt.title("Sobel x:"), plt.axis("off")
plt.subplot2grid((5, 2), (1, 1)), plt.imshow(sy2, cmap="gray"), plt.title("Sobel y:"), plt.axis("off")
plt.subplot2grid((5, 2), (2, 1)), plt.imshow(sob2, cmap="gray"), plt.title("Sobel Edge Detection:"), plt.axis("off")
plt.subplot2grid((5, 2), (3, 1)), plt.imshow(t2, cmap="gray"), plt.title("After Inverse Thresholding:"), plt.axis("off")


plt.savefig("C:/Users/akalf/Documents/Sobel.png", format="png", dpi=1200)
