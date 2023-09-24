# importing libraries
import cv2
import numpy as np
import os
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('vid.mp4')

path_avg = 'q2_video'
index=0
# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video  file")

video_file = 'q2_video/video.mp4'
image_size = (360, 640, 3)
fps = 24
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('q2_video/video.mp4',apiPreference = 0, fourcc=fourcc, fps=30,frameSize=(360,640))
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
#creating an object of videoWriter for writing video
out = cv2.VideoWriter('output_video.avi',fourcc, 30, (int(cap.get(3)),int(cap.get(4))))
# Read until video is completed
while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    # print(frame.size)
    if ret == False:
        break

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # apply a blur using the median filter
    img = cv2.medianBlur(img, 13)
    # edges = canny(img, sigma=2.0, low_threshold=0.55, high_threshold=0.8)
    # find circles in grayscale image using the Hough transform
    circles = cv2.HoughCircles(image=img, method=cv2.HOUGH_GRADIENT, dp=0.9,
                               minDist=50, param1=70, param2=55, maxRadius=60)

    if np.any(circles):
        print("------------------")
        print("number of circles: ", len(circles[0, :]))
        for co, i in enumerate(circles[0, :], start=1):
            # draw the outer circle with radius i[2] in green
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 0, 255), 3)
            # draw the center as a circle with radius 2 in red
            cv2.circle(frame, (i[0], i[1]), 2, (255, 0, 0), 3)
            print("center of circle: ", i[0], ", ", i[1])
    else:
        print("No circles detected.")
    # show image
    # cv2.imwrite(os.path.join(path_avg, str(index) + '.jpg'), frame)
    out.write(frame)
    cv2.imshow('Video', frame)
    index=index+1
    # While video window is active, press 'q' on the keyboard to quit
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


# When everything done, release
# the video capture object
cap.release()
out.release()
# Closes all the frames
cv2.destroyAllWindows()