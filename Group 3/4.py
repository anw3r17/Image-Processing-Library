import cv2
import matplotlib.pyplot as plt
import textwrap

# Reading image
img = cv2.imread("C:/Users/akalf/Documents/Lenna.png")

# Convert BGR to GRAY
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Laplacion Operator
lap = cv2.Laplacian(img1, cv2.CV_64F)

# Inverse Thresholding
ret, t1 = cv2.threshold(lap, 20, 255, cv2.THRESH_BINARY_INV)

# Denoise the image
dn = cv2.GaussianBlur(img1, (3, 3), 0)

# Apply Laplacion on Denoised Image
lap1 = cv2.Laplacian(dn, cv2.CV_64F)

# Inverse Thresholding 
ret, t2 = cv2.threshold(lap1, 20, 255, cv2.THRESH_BINARY_INV)

# Display all the Images
plt.subplot(331).set_title("\n".join(textwrap.wrap("Grayscale Image", 20))), plt.imshow(img1), plt.axis("off")
plt.subplot(332).set_title("\n".join(textwrap.wrap("Laplacian Edge Detection", 20))), plt.imshow(lap), plt.axis("off")
plt.subplot(333).set_title("\n".join(textwrap.wrap("After Inverse Thresholding", 20))), plt.imshow(t1), plt.axis("off")
plt.subplot(337).set_title("\n".join(textwrap.wrap("Denoised Image", 20))), plt.imshow(dn), plt.axis("off")
plt.subplot(338).set_title("\n".join(textwrap.wrap("Laplacian Edge Detection on Denoised Image", 20))), plt.imshow(lap1), plt.axis("off")
plt.subplot(339).set_title("\n".join(textwrap.wrap("After Inverse Thresholding", 20))), plt.imshow(t2), plt.axis("off")

plt.savefig("C:/Users/akalf/Documents/Laplacian.png", format = "png", dpi = 1200)
