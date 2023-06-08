import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from matplotlib.colors import LogNorm
from scipy import *

# Reading The Image
srcImage = plt.imread("images/moonlanding.png").astype(float)
# astype() methods converts numerical string or numbers to the float values as possible

# displaying the orignal image
plt.figure()
plt.imshow(srcImage,plt.cm.gray) #plt.cm.gray , diplays the image in gray color palatte  
plt.title("Source Image")
plt.show()


# Cleaning up the noise
# Computing the 2D FFT Of The Image
fftImage = fftpack.fft2(srcImage)
plt.imshow(np.abs(fftImage),norm=LogNorm(vmin=5))
plt.colorbar()
plt.title("Fourier Transform Of Image")
plt.show()


# Constant for keeping the component frequencies
constantFraction = 0.1

# Creating copy of FFT-Images
fftImage1 = fftImage.copy()
# calculating the number of rows and columns by shape property of the imageMatrix
row,column = fftImage1.shape

# In Image Matrix Setting all elements in row to zeros whose index are in the range of
# row*constantFraction to row*(1-constantFraction) using the array slicing method
fftImage1[int(row*constantFraction):int(row*(1-constantFraction))] = 0

# In Image Matrix Setting all elements in column to zeros whose index are in the range of
# column*constantFraction to column*(1-constantFraction)
fftImage1[:, int(column*constantFraction):int(column*(1-constantFraction))] = 0

# Plotting the figure
plt.figure()
plt.imshow(np.abs(fftImage1),norm=LogNorm(vmin=5))
plt.colorbar()
plt.title("Filtered Spectrum")
plt.show()

# Denoising the image from the Filtered Spectrum by keeping the real part for the display
newImage = fftpack.ifft2(fftImage1).real
plt.figure()
plt.imshow(newImage,plt.cm.gray)
plt.title("Denoised Image")
plt.show()
