import sys, getopt
import numpy as np
import cv2
import constantes as c 
from imagen import Imagen

def ecualizar(gray):
  #gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
  eq=cv2.equalizeHist(gray)
  return eq

def detectFaceRects(gray,cascade):
  rects = detect(gray, cascade)
  if(rects==[]):
    img=Imagen(gray).blur(c.detectFaceBlur)
    rects = detect(img.imagen, cascade)
  return rects

def detectEyes(x1,y1,x2,y2,gray,vis):
  #el principal solo detecta 7 casos! TODO ......
  subrects=[]
  nested = cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+"haarcascade_eye.xml")
  roi = gray[y1:y2, x1:x2]
  vis_roi = vis[y1:y2, x1:x2]
  subrects = detect(roi.copy(), nested)
  if len(subrects)==2:
    print"PRINCIPAL"
  if len(subrects)<2:#detectamos los ojos por separado TODO -> no detecta nada!
    nested = cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+"haarcascade_lefteye_2splits.xml")
    subrectsL = detect(roi.copy(), nested)
    nested = cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+"haarcascade_righteye_2splits.xml")
    subrectsR = detect(roi.copy(), nested)
    subrects=subrectsL+subrectsL
    if len(subrects)==2:
      print"POR SEPARADO"
  if len(subrects)<2:#o que sean muy peq TODO -> no detecta nada!
    nested = cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+"haarcascade_mcs_eyepair_small.xml")
    subrects = detect(roi.copy(), nested)
    if len(subrects)==2:
      print"OJOS PEQ"
  if len(subrects)<2:#o que sean muy grandes TODO no detecta ningun caso
    nested = cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+"haarcascade_mcs_eyepair_big.xml")
    subrects = detect(roi.copy(), nested)
    if len(subrects)==2:
      print"OJOS GRANDES"
  return subrects,vis_roi

def detectMouth(x1,y1,x2,y2,gray,vis):
  mouth= cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+c.boca)
  roi = gray[y1:y2, x1:x2]
  vis_roi = vis[y1:y2, x1:x2]
  subrects = detect(roi.copy(), mouth)
  if subrects== []:
    mouth=cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+c.boca2)
    grayL=cv2.Laplacian(gray,cv2.CV_8U)
    gray=gray-grayL
    ecualizar(gray)
    gray=Imagen(gray).gaussianFilter(13,13,1).imagen
    roi = ecualizar(gray[y1:y2, x1:x2])
    vis_roi = vis[y1:y2, x1:x2]
    subrects = detect(roi.copy(), mouth)
  return subrects,vis_roi

def detectNose(x1,y1,x2,y2,gray,vis):
  nose= cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+c.nariz)
  gray=Imagen(gray).blur(c.detectFaceBlur).imagen
  roi = gray[y1:y2, x1:x2]
  vis_roi = vis[y1:y2, x1:x2]
  subrects = detect(roi.copy(), nose)
  return subrects,vis_roi

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(25, 25), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]	
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

def seleccionaMenor(subrects):
  area=999999
  menor=[]
  for rect in subrects:
    x=rect[2]-rect[0]
    y=rect[3]-rect[1]
    if x*y<area:
      area=x*y
      menor=[rect]
  return menor

def detectFace(img,name,cascadeFilter="haarcascade_frontalface_default.xml",nestedFilter="haarcascade_eye.xml"):
  #devuelve la imagen con la cara , la region ocular marcada  y un dict con rectangulos 
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray = cv2.equalizeHist(gray)
  cascade= cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+cascadeFilter)
  rects=detectFaceRects(gray,cascade)
  vis = img.copy()
  draw_rects(vis, rects, (0, 0, 255))
  #para cada cara detectada, detectamos sus ojos.
  detector=0
  todo=False
  for x1, y1, x2, y2 in rects:
    detector=0;
    subrects,vis_roi=detectMouth(x1,(y1-y2)*2/3,x2,y2,gray,vis)
    if len(subrects)>=1:
      subrects=seleccionaMenor(subrects)
      detector+=1
    draw_rects(vis_roi, subrects, (0, 255, 0))
    subrects,vis_roi=detectEyes(x1,y1,x2,(y1-y2)*4/8,gray,vis)
    if len(subrects)>=1:
      detector+=1
    draw_rects(vis_roi, subrects, (0, 255, 255))
    subrects,vis_roi=detectNose(x1,y1,x2,y2,gray,vis)
    if len(subrects)>=1:
      detector+=1
    """x=x2-x1
    y=y2-y1
    (x1,y1,x2,y2)=subrects[0]
    xc=(x2-x1)/2
    yc=(y2-y1)/2  
    print x,y,xc,yc
    print name+"\n"  """
    if detector==3:
      todo=True
    draw_rects(vis_roi, subrects, (255, 0, 0))
  return vis,todo


