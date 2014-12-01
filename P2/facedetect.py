import sys, getopt
import numpy as np
import cv2
import constantes as c 
from imagen import Imagen
import types

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

def haz_simetrico(subrectsR,subrectsL,cara): #TODO arreglar esto!  
  (x1,y1,x2,y2)=cara
  centro=x2-x1
  if len(subrectsR)==0:
    subrectsR=np.array([subrectsL[0][0]+abs(centro-subrectsL[0][0]),subrectsL[0][1],subrectsL[0][2]+abs(centro-subrectsL[0][2]),subrectsL[0][3]], dtype=np.int32)
    print subrectsL
    return np.array([[subrectsR[0],subrectsR[1],subrectsR[2],subrectsR[3]],[subrectsL[0],subrectsL[1],subrectsL[2],subrectsL[3]]],dtype=np.int32)
  if len(subrectsL)==0:
    subrectsL=np.array([subrectsR[0][0]-abs(centro-subrectsR[0][0]),subrectsR[0][1],subrectsR[0][2]-abs(centro-subrectsR[0][2]),subrectsR[0][3]], dtype=np.int32)
    print subrectsL
    return np.array([[subrectsR[0],subrectsR[1],subrectsR[2],subrectsR[3]],[subrectsL[0],subrectsL[1],subrectsL[2],subrectsL[3]]],dtype=np.int32)
  return np.array([])

def ojos_separados(x1,y1,x2,y2,gray):
  #detectamos los ojos por separado TODO -> no detecta nada!
  roi = gray[y1:y2, x1:x2]
  nested = cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+"haarcascade_lefteye_2splits.xml")
  subrectsL = detect(roi.copy(), nested,1.1)
  subrectsL=seleccionaMenor(subrectsL)
  nested = cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+"haarcascade_righteye_2splits.xml")
  subrectsR = detect(roi.copy(), nested,1.1)
  subrectsR=seleccionaMenor(subrectsR)
  subrects=subrectsL+subrectsL
  if len(subrectsR)==1 and len(subrectsL)==1:
    print "ojos separados"
    return subrects
  if len(subrectsR)==1 or len(subrectsL)==1:
    cara=(x1,y1,x2,y2)
    print "hacer simetrico"
    #return haz_simetrico(subrectsR,subrectsL,cara)
    return subrects
    

def ojos_grandes(x1,y1,x2,y2,gray):
  #gray=Imagen(gray).gaussianFilter(17,17,1).imagen
  roi = gray[y1:y2, x1:x2]
  nested = cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+"haarcascade_mcs_eyepair_big.xml")
  subrects = detect(roi.copy(), nested,1.1)
  if len(subrects)==0:
    gray=Imagen(gray).gaussianFilter(5,5,1).imagen
    roi = gray[y1:y2, x1:x2]
    subrects = detect(roi.copy(), nested,1.1)
  return subrects

def ojos_peq(x1,y1,x2,y2,gray):
  roi = gray[y1:y2, x1:x2]
  nested = cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+"haarcascade_mcs_eyepair_small.xml")
  subrects = detect(roi.copy(), nested,1.1)
  if len(subrects)==0:
    gray=Imagen(gray).gaussianFilter(5,5,1).imagen
    roi = gray[y1:y2, x1:x2]
    subrects = detect(roi.copy(), nested,1.1)
  return subrects

def ojos_gafas(x1,y1,x2,y2,gray):
  roi = gray[y1:y2, x1:x2]
  nested = cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+"haarcascade_eye_tree_eyeglasses2.xml")
  subrects = detect(roi.copy(), nested,1.1)
  if len(subrects)==0:
    nested = cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+"haarcascade_eye_tree_eyeglasses.xml")
    gray=Imagen(gray).gaussianFilter(5,5,0).imagen
    roi = gray[y1:y2, x1:x2]
    roi=ecualizar(roi)
    subrects = detect(roi.copy(), nested,1.1)
  return subrects

def ojos_normales(x1,y1,x2,y2,roi):
    nested = cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+"haarcascade_eye.xml")
    subrects = detect(roi.copy(),nested,(1.1))
    return subrects 


def detectEyes2(x1,y1,x2,y2,gray,vis):
  subrects=[]
  roi = gray[y1:y2, x1:x2]
  vis_roi = vis[y1:y2, x1:x2]
  subrects=ojos_normales(x1,y1,x2,y2,roi)
  if len(subrects)==2:
    return subrects,vis_roi
  roi=ecualizar(roi)
  subrects=ojos_normales(x1,y1,x2,y2,roi)
  if len(subrects)==2:
    return subrects,vis_roi
  roi = gray[y1:y2, x1:x2]
  roi=ecualizar(roi)
  roi=Imagen(roi).blur("gaussian").imagen
  subrects=ojos_normales(x1,y1,x2,y2,roi)
  if len(subrects)==2:
    return subrects,vis_roi
  roi = gray[y1:y2, x1:x2]
  roi=Imagen(roi).blur("gaussian").imagen
  subrects=ojos_normales(x1,y1,x2,y2,roi)
  if len(subrects)==2:
    return subrects,vis_roi
  subrects,vis_roi=detectEyes(x1,y1,x2,y2,gray,vis)
  return subrects,vis_roi

def detectEyes(x1,y1,x2,y2,gray,vis):
  subrects=[]
  roi = gray[y1:y2, x1:x2]
  vis_roi = vis[y1:y2, x1:x2]
  subrects=ojos_normales(x1,y1,x2,y2,roi)
  if len(subrects)==2:
    print "normales "
    return subrects,vis_roi
  #ojos peq
  subrects=ojos_peq(x1,y1,x2,y2,gray)
  if not type(subrects)==types.NoneType:
    if len(subrects)==2:
      print "ojos peq!"
      return subrects,vis_roi
  #ojos grandes
  subrects = ojos_grandes(x1,y1,x2,y2,gray)
  if not type(subrects)==types.NoneType:
    if len(subrects)==2:
      print "ojos grandes!"
      return subrects,vis_roi
  #ojos separados
  subrects=ojos_separados(x1,y1,x2,y2,gray)
  if not type(subrects)==types.NoneType:
    if len(subrects)==2:
      return subrects,vis_roi
  #ojos con gafas
  subrects=ojos_gafas(x1,y1,x2,y2,gray)
  if not type(subrects)==types.NoneType:
    if len(subrects)==1:
      print "gafas"
      return subrects,vis_roi
  return [],vis_roi

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

def detect(img, cascade,scale=1.3):
    rects = cascade.detectMultiScale(img, scaleFactor=scale, minNeighbors=4, minSize=(25, 25), flags = cv2.CASCADE_SCALE_IMAGE)
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

def detectCara(gray):
  cascade= cv2.CascadeClassifier(c.cascadeFilterFolder+"/"+c.cascadeFilter)
  rects=detectFaceRects(gray,cascade)
  return rects


def detectFace(img,name,nestedFilter="haarcascade_eye.xml"):
  #devuelve la imagen con la cara , la region ocular marcada  y un dict con rectangulos 
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  rects=detectCara(gray)
  vis = img.copy()
  draw_rects(vis, rects, (0, 0, 255))
  #para cada cara detectada, detectamos sus ojos.
  detector=0
  todo=False
  for x1, y1, x2, y2 in rects:
    detector=0;
    #boca
    subrects,vis_roi=detectMouth(x1,(y1-y2)*4/6,x2,y2,gray,vis)
    if len(subrects)>=1:
      subrects=seleccionaMenor(subrects)
      detector+=1
    draw_rects(vis_roi, subrects, (0, 255, 0))
    #ojos
    subrects,vis_roi=detectEyes2(x1,y1,x2,(y1-y2)*3/5,gray,vis)
    if len(subrects)>1:
      detector+=1
    draw_rects(vis_roi, subrects, (0, 255, 255))
    #nariz
    subrects,vis_roi=detectNose(x1,y1,x2,y2,gray,vis)
    if len(subrects)>=1:
      subrects=seleccionaMenor(subrects)
      detector+=1
    if detector==3:
      todo=True
    draw_rects(vis_roi, subrects, (255, 0, 0))
  return vis,todo


