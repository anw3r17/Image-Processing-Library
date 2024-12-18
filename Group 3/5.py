import cv2
import numpy as np

# Reading image
img = cv2.imread("C:/Users/akalf/Documents/Lenna.png")

# Convert BGR to GRAY
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Compute the Direct Cosine Transform
dct = cv2.dct(np.float32(img1), cv2.DCT_INVERSE)

# Inverse DCT
idctimg = cv2.idct(dct)

# Convert to uint8
idct = np.uint8(idctimg)

#Display the images
cv2.imshow("Original Image:", img1)
cv2.imshow("Consine Transform Image:", dct)
cv2.imshow("Inverted Consine Transfrom Image:", idct)

cv2.waitKey(0)
cv2.destroyAllWindows()

