import cv2 as cv
import numpy as np

## CPU
cap = cv.VideoCapture(0)


while(True):

    ## CPU
    ret, cpu_frame = cap.read()

    if ret == True:
        cv.imshow('frame', cpu_frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cv.destroyAllWindows()