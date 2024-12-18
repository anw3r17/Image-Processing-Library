import cv2

# Reading image
img = cv2.imread("C:/Users/akalf/Documents/Lenna.png")

# Convert to GRAYSCALE
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Thresholding
ret, t1 = cv2.threshold(img1, 120, 255, cv2.THRESH_BINARY)
ret, t2 = cv2.threshold(img1, 120, 255, cv2.THRESH_BINARY_INV)
ret, t3 = cv2.threshold(img1, 120, 255, cv2.THRESH_TRUNC)
ret, t4 = cv2.threshold(img1, 120, 255, cv2.THRESH_TOZERO)
ret, t5 = cv2.threshold(img1, 120, 255, cv2.THRESH_TOZERO_INV)

# 2 methods to display the thresholding, either use imshow() or plotting through matplotlib
cv2.imshow("Binary Threshold", t1)
cv2.imshow("Binary Threshold Inverted", t2)
cv2.imshow("Truncated Threshold", t3)
cv2.imshow("Set to 0 Threshold", t4)
cv2.imshow("Set to 0  Inverted Threshold", t5)

cv2.waitKey(0)
cv2.destroyAllWindows()



