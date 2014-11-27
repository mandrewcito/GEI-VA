import cv2
import numpy as np
from matplotlib import pyplot as plt
from imagen import Imagen
import os,sys

def coincidencias(keypoints,keypoints2):
  coincidencias=0
  for kp in keypoints:
    for kp2 in keypoints2:
      if abs(kp.pt[0]-kp2.pt[0])<1 and abs(kp.pt[1]-kp2.pt[1]) and abs(kp.response-kp2.response)<1:
        coincidencias+=1
  return coincidencias

def main():
  args = sys.argv[1:]
  sujeto1=args[0]
  sujeto2=args[1]
  im=Imagen("image-"+sujeto1+".jpg")
  im1=Imagen("image-"+sujeto2+".jpg")
  orb=cv2.ORB()
  keypoints=orb.detect(im.imagen)
  keypoints1=orb.detect(im1.imagen)
  cv2.drawKeypoints(im.imagen,keypoints,im.imagen)
  cv2.drawKeypoints(im1.imagen,keypoints1,im1.imagen)
  if coincidencias(keypoints1,keypoints)>40:
    print True
  else:
    print False

if __name__ == "__main__":
    main()


