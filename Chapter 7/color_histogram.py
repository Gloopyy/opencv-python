from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

#Split image into channels
chans = cv2.split(image)
colors = ("b", "g", "r")

#Make graph
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

#Loop once for each channel in image
for (chan, color) in zip(chans, colors):
    #Compute histogram
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    #Add histogram to existing graph
    plt.plot(hist, color = color)
    plt.xlim([0, 256])

fig = plt.figure()

ax = fig.add_subplot(131)
#Use green and blue channels for histogram
#32 bins
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

plt.show()