import cv2
import numpy as np 
from imagen import Imagen

#mide lo cuadrado que es algo dados sus lados 
def esPocoCuadrado(lado1,lado2):
  margenErr = 0.45
  ladoGrande = lado1
  ladoPeq = lado2 
  if lado1 < lado2: 
    ladoGrande = lado2
    ladoPeq = lado1  
  return float(ladoPeq)/float(ladoGrande) < margenErr


#recibe un rectangulo que envuelve el contorno y evalua su proporcion
def proporcionesCorrectas(rect):
  x,y = rect[0]
  w,h = rect[1]
  angulo = rect[2]
  print angulo
  if not esPocoCuadrado(int(w), int(h)) and abs(angulo) <= 10.0:
    return True
  return False


# recibe un contorno cuadrilatero, si un porcentaje es del color correcto devuelve true, onpencvColor (B,G,R)
def colorCorrecto(img,cnt): 
  mask = np.zeros(img.shape[:2],np.uint8)
  cv2.drawContours(mask,[cnt],0,255,-1)
  mean_val = cv2.mean(img,mask = mask)
  if mean_val[0]<100 and mean_val[1]<130 and mean_val[2]>130:
      return True
  else:
      return False 



def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def find_badSquare(imgOrig):
  squares =[]
  img = cv2.inRange(imgOrig, (52,40,190), (255, 140,255))
  kernel = np.ones((3,3), np.uint8)
  kernel1 = np.ones((2,2), np.uint8)
  kernel2 = np.ones((5,5), np.uint8)    
  #bin = cv2.closing(bin, kernel)   
  bin = cv2.morphologyEx(img, cv2.MORPH_CLOSE,kernel2)  
  
  #bin = cv2.morphologyEx(bin, cv2.MORPH_ERODE,kernel1)
  bin = cv2.morphologyEx(bin, cv2.MORPH_OPEN,kernel2)
  bin = cv2.morphologyEx(bin, cv2.MORPH_DILATE,kernel2) 

  #bin = cv2.morphologyEx(bin, cv2.MORPH_CLOSE,kernel2)  
  
  Imagen(bin).show()  
  bin = cv2.Canny(bin, 25, 350, apertureSize=3)
  #bin = cv2.morphologyEx(bin, cv2.MORPH_DILATE, kernel1)
       
  contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)        
  for cnt in contours:
    #contornos cerrados 
    cnt_len = cv2.arcLength(cnt, True)
    epsilon = 0.020*cv2.arcLength(cnt,True)
    cnt = cv2.approxPolyDP(cnt, epsilon, True)
    if len(cnt) >= 6 and cv2.contourArea(cnt) > 300  :
      cnt = cnt.reshape(-1, 2)
      max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
      #if max_cos < 0.7: 
      squares.append(cnt)
  return squares

def find_squares(imgOrig):
  img = cv2.inRange(cv2.GaussianBlur(imgOrig, (3, 3), 0.5), (0,0,150), (100, 100, 200))
  squares = []
  #bin = cv2.Canny(img, 25, 350, apertureSize=3)
  kernel = np.ones((3,3), np.uint8)
  kernel1 = np.ones((5,5), np.uint8)
  #bin = cv2.closing(bin, kernel)   
  bin = cv2.morphologyEx(img, cv2.MORPH_CLOSE,kernel)  
  bin = cv2.morphologyEx(bin, cv2.MORPH_DILATE,kernel1) 
  bin = cv2.Canny(bin, 25, 350, apertureSize=3)
  bin = cv2.morphologyEx(bin, cv2.MORPH_DILATE, kernel1)
  Imagen(bin).show()              
  contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)        
  for cnt in contours:
    #contornos cerrados 
    cnt_len = cv2.arcLength(cnt, True)
    epsilon = 0.030*cv2.arcLength(cnt,True)
    cnt = cv2.approxPolyDP(cnt, epsilon, True)
    if len(cnt) == 4 and cv2.contourArea(cnt) > 200 and cv2.contourArea(cnt) <1700 and cv2.isContourConvex(cnt) and proporcionesCorrectas(cv2.minAreaRect(cnt)):
      cnt = cnt.reshape(-1, 2)
      max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
      if max_cos < 0.7: 
        squares.append(cnt)
  return squares
