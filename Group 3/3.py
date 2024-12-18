import cv2
import numpy as np

# Reading image
img = cv2.imread("C:/Users/akalf/Documents/Lenna.png")

# Convert BGR to GRAY
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Compute the Direct Fourier Transform
dft = cv2.dft(np.float32(img1), flags = cv2.DFT_COMPLEX_OUTPUT)

# Compute the Magnitude 
mag = 20 * np.log(cv2.magnitude(dft[:, :, 0], dft[:, :, 1]))

# Normazlize the Magnitude to Display it
mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

# Compute Inverse DFT
idft = cv2.idft(dft)

# Compute Inverted Magnitude
imag = 20 * np.log(cv2.magnitude(idft[:, :, 0], idft[:, :, 1]))

# Nomalize IMAG for display purposes
imag = cv2.normalize(imag, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

# Display the Magnitude of DFT
cv2.imshow("Original Image:", img1)
cv2.imshow("Direct Fourier Transform:", mag)
cv2.imshow("Magnitude Spectrum:", imag)

cv2.waitKey(0)
cv2.destroyAllWindows()

