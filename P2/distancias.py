import cv2
import numpy as np
from matplotlib import pyplot as plt
from imagen import Imagen
import os,sys
import facedetect as f
#TODO en desarrollo -------------------- JESUS QUE MAL VA

def distancias(gray,vis):
  rects=f.detectCara(gray)
  x1c, y1c, x2c, y2c=rects[0]
  centrocara=((x2c-x1c)/2)
  subrects,vis_roi=f.detectMouth(x1c,(y1c-y2c)*2/3,x2c,y2c,gray,vis)
  x1, y1, x2, y2=subrects[0]
  centrox=((x2-x1)/2)+x1
  centroy=((y2-y1)/2)+y1
  boca=(centrox,centroy)
  subrects,vis_roi=f.detectNose(x1c,y1c,x2c,y2c,gray,vis)
  x1, y1, x2, y2=subrects[0]
  centrox=((x2-x1)/2)+x1
  centroy=((y2-y1)/2)+y1
  nariz=(centrox,centroy)
  subrects,vis_roi=f.detectEyes2(x1c,y1c,x2c,(y1c-y2c)*3/5,gray,vis)
  x1, y1, x2, y2=subrects[0]
  centrox=((x2-x1)/2)+x1
  centroy=((y2-y1)/2)+y1
  ojo1=(centrox,centroy)
  x1, y1, x2, y2=subrects[1]
  distancia=abs(centrocara-centrox)
  if centrox!=((x2-x1)/2)+x1:  
    centrox=((x2-x1)/2)+x1
  if centrox==((x2-x1)/2)+x1 and centrox>centrocara:
    centrox=centrox-2*distancia
  elif centrox==((x2-x1)/2)+x1 and centrox<centrocara:
    centrox=centrox+2*distancia  
  centroy=((y2-y1)/2)+y1
  ojo2=(centrox,centroy)
  return boca,nariz,ojo1,ojo2

def area(v1,v2,v3):
  #hacemos area teniendo en cuenta que v2,v3 son la base
  #     |x  y  1|
  # 1/2 |x1 y1 1| = area
  #     |x2 y2 1|
  x,y=v1
  x1,y1=v2
  x2,y2=v3
  #print v1,v2,v3
  area=abs((x*y1)+(y*x2)+(x1*y2)-(x2*y1)-(x1*y)-(y2*x))/2
  #print area
  return area
  
def areas(boca,nariz,ojo1,ojo2):
  a1=area(nariz,ojo1,ojo2)
  a2=area(boca,ojo1,ojo2)
  return a1,a2

def comparaAreas(a1,a2,b1,b2,umbral):
  if abs(a1-b1)<umbral and abs(a2-b2)<umbral: 
    return True
  return False
  #return "suejo1 "+str(a1)+"  "+str(a2)+" suejo2 "+str(b1)+"  "+str(b2)

def main():
  args = sys.argv[1:]
  sujeto1=args[0]
  sujeto2=args[1]
  umbral=args[2]
  im=Imagen("image-"+sujeto1+".jpg")
  im1=Imagen("image-"+sujeto2+".jpg")
  vis = im.imagen.copy()
  vis1 = im1.imagen.copy()
  gray = cv2.cvtColor(im.imagen, cv2.COLOR_BGR2GRAY)
  gray1 = cv2.cvtColor(im1.imagen, cv2.COLOR_BGR2GRAY)
  boca,nariz,ojo1,ojo2=distancias(gray,vis)
  sujeto1Area1,sujeto1Area2=areas(boca,nariz,ojo1,ojo2)
  boca,nariz,ojo1,ojo2=distancias(gray1,vis1)
  sujeto2Area1,sujeto2Area2=areas(boca,nariz,ojo1,ojo2)
  print comparaAreas(sujeto1Area1,sujeto1Area2,sujeto2Area1,sujeto2Area2,int(umbral))
if __name__ == "__main__":
    main()

