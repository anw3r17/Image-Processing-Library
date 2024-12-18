import cv2

img = cv2.imread("C:/Users/akalf/Documents/Lenna.png")

# Get dimensions of the image
d = img.shape
w = img.shape[0]
h = img.shape[1]
c = img.shape[2]

# Print image dimensions

print("Dimensions of the Image: ", d)
print("Height of the Image: ", w)
print("Width of the Image: ", h)
print("Number of Channels of the Image: ", c)

# Convert to grayscale using pixel manipulation (Average Method)
for i in range(h):
    for j in range(w):
        # Calculate the average of the BGR pixel values
        avg = int(sum(img[i, j]) * 0.33)
        img[i, j] = (avg, avg, avg)  # Set the same average value for all channels
        
# Display the grayscale img

cv2.imshow("Grayscale Image:", img)

# Wait for a key press and close the window

cv2.waitKey(0)
cv2.destroyAllWindows()