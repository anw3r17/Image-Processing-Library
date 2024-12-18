import cv2 
#Read the img

img = cv2.imread("C:/Users/akalf/Documents/Lenna.png", cv2.IMREAD_COLOR)
#showing the img

cv2.imshow("Image: ", img)
#checking keys

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("C:/Users/akalf/DIPLAB/newimg.png", img)
    cv2.destroyAllWindows()
