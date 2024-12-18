# Import opencv
import cv2

# Load the input image
img = cv2.imread("C:/Users/akalf/Documents/Lenna.png")

# Split the image into BGR
B, G, R = cv2.split(img)

# Print the Image and BGR channels
cv2.imshow("Image:", img)
cv2.waitKey(0)
cv2.imshow("Blue:", B)
cv2.waitKey(0)
cv2.imshow("Green:", G)
cv2.waitKey(0)
cv2.imshow("Red:", R)
cv2.waitKey(0)
cv2.destroyAllWindows()
