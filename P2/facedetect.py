import sys, getopt
import numpy as np
import cv2
import constantes as c 

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

def detectFace(img,cascadeFilter="haarcascade_frontalface_alt.xml",nestedFilter="haarcascade_eye.xml"):
  #devuelve la imagen con la cara , la region ocular marcada  y rectangulos 
  cascade= cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+cascadeFilter)
  nested = cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+nestedFilter)
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
  return vis,rects
