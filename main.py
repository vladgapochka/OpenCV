import math
import cv2
import numpy as np


img1 = cv2.imread(r'C:\Users\gapoc\Desktop\1539076209_18.jpg', -1)
cv2.namedWindow('Display window', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Display window',img1)
cv2.waitKey(0)


cap = cv2.VideoCapture(r'C:\Users\gapoc\Downloads\viz.mp4', cv2.CAP_ANY)
while True:
    ret,frame=cap.read()
    if not(ret):
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()

def readIPWriteTOFile():
    video = cv2.VideoCapture("http://192.168.43.1:8080/video")
    ok, img = video.read()
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("output.mov", fourcc, 25, (w, h))
    while (True):
        ok, img = video.read()
        cv2.imshow('img', img)
        video_writer.write(img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()
# readIPWriteTOFile()
def print_cam():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    while True:
        ret, frame = cap.read()
 # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == 27:
            break
