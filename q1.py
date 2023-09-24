import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

im = cv2.imread('sudoku.jpg')
print(im)
print(im.shape)
plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
plt.title("original image")
plt.figure()
# plt.show()
im=im[:600,:]
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# Find the edges in the image using canny detector
edges = cv2.Canny(gray, 50, 200)
# Detect points that form a line
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=10, maxLineGap=250)
# Draw lines on the image
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(im, (x1, y1), (x2, y2), (255, 0, 0), 3)

# Show result
# img = cv2.resize(im, dsize=(600, 600))
plt.imshow(im)
plt.title("result image")
plt.show()