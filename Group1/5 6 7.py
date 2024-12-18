import cv2

# Reading image
img = cv2.imread("C:/Users/akalf/Documents/Lenna.png")

# Conversions from COLOR to GRAYSCALE, BGR to RGB, BGR to HSV
cg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
br = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
bh = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Display all the conversions
cv2.imshow("COLOR TO GRAYSCALE", cg)
cv2.imshow("BGR TO RGB", br)
cv2.imshow("BGR TO HSV", bh)
cv2.waitKey(0)
cv2.destroyAllWindows()
