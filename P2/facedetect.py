#!/usr/bin/env python
import sys, getopt
import numpy as np
import cv2
#TODO hacer de esto una funcion decente no un script 
def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
  cascade= cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
  nested = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
  img=cv2.imread("Biometria/jpg/image-9.jpg")
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray = cv2.equalizeHist(gray)
  rects = detect(gray, cascade)
  vis = img.copy()
  draw_rects(vis, rects, (0, 0, 255))
  for x1, y1, x2, y2 in rects:
    roi = gray[y1:y2, x1:x2]
    vis_roi = vis[y1:y2, x1:x2]
    subrects = detect(roi.copy(), nested)
    draw_rects(vis_roi, subrects, (255, 0, 0))
  cv2.imshow('facedetect', vis)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
