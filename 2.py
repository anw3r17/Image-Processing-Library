import cv2
#reading color image

img = cv2.imread("C:/Users/akalf/Documents/Lenna.png", cv2.IMREAD_COLOR)
#reading grayscale image

img_g = cv2.imread("C:/Users/akalf/Documents/Lenna.png", cv2.IMREAD_GRAYSCALE)

#display

cv2.imshow("Image: ", img)
#key checking

k = cv2.waitKey(0)
if k == ord('g'):
    cv2.imwrite("C:/Users/akalf/DIPLAB/newimg.png", img_g)
    cv2.destroyAllWindows()
elif k == ord('c'):
    cv2.imwrite("C:/Users/akalf/DIPLAB/newimg.png", img)
    cv2.destroyAllWindows()
    
