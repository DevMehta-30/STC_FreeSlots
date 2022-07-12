import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.png')   # you can read in images with opencv
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsv_color1 = np.asarray([0, 200, 255])   # white!
hsv_color2 = np.asarray([0, 250, 255])   # yellow! note the order

mask = cv2.inRange(img_hsv, hsv_color1, hsv_color2)

cv2.imwrite("green.png",mask)
plt.imshow(mask,cmap='gray')   # this colormap will display in black / white
plt.show()

