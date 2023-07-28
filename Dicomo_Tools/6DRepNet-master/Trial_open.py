import numpy as np
import cv2 as cv
from tqdm import tqdm
cap = cv.VideoCapture('./video/MinYen1_trim.mp4')
if not cap.isOpened():
    print("Cannot open camera")
    exit()
length = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

for i in tqdm(range(length)):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    #cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()