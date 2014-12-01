import cv2
import numpy as np
from matplotlib import pyplot as plt
from imagen import Imagen
import os,sys
import facedetect as f
#TODO en desarrollo --------------------

def coincidencias(keypoints,keypoints2,zona,zona2):
  coincidencias=0
  for kp in keypoints:
    if zona[0]<kp.pt[0]and kp.pt[1]>zona[1]and kp.pt[1]<zona[2] and kp.pt[1]<zona[3]: #esta en zona?
      for kp2 in keypoints2:
        if kp.pt[0]==kp2.pt[0] and kp.pt[1]==kp2.pt[1] and abs(kp.response-kp2.response)<1:#coinciden?
          coincidencias+=1
  return coincidencias

def main():
  args = sys.argv[1:]
  sujeto1=args[0]
  sujeto2=args[1]
  im=Imagen("image-"+sujeto1+".jpg")
  im1=Imagen("image-"+sujeto2+".jpg")
  gray = cv2.cvtColor(im.imagen, cv2.COLOR_BGR2GRAY)
  gray1 = cv2.cvtColor(im1.imagen, cv2.COLOR_BGR2GRAY)
  orb=cv2.ORB()
  vis = im.imagen.copy()
  vis1 = im1.imagen.copy()

  #
  rects=f.detectCara(gray)
  x1c, y1c, x2c, y2c=rects[0]
  subrects,vis_roi=f.detectMouth(x1c,(y1c-y2c)*2/3,x2c,y2c,gray,vis)
  x1, y1, x2, y2=subrects[0]
  keypoints=orb.detect(im.imagen)
  zona=(x1c+x1,y1c+y1,x2c+x2,y2c+y2)
  #
  rects=f.detectCara(gray)
  x1, y1, x2, y2=rects[0]
  subrects,vis_roi=f.detectMouth(x1,(y1-y2)*2/3,x2,y2,gray1,vis1)
  x1, y1, x2, y2=subrects[0]
  keypoints1=orb.detect(im1.imagen)
  zona2=(x1c+x1,y1c+y1,x2c+x2,y2c+y2)
  cv2.drawKeypoints(im.imagen,keypoints,im.imagen)
  cv2.drawKeypoints(im1.imagen,keypoints1,im1.imagen)
  c=coincidencias(keypoints1,keypoints,zona,zona2)
  if c>10:
    print True
  else:
    print False

if __name__ == "__main__":
    main()


