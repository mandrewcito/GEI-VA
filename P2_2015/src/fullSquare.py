#!/usr/bin/env python
#coding=utf8

import numpy as np
import cv2,os
from matplotlib import pyplot as plt
from imagen import Imagen
import libSquares as ls

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
    if not esPocoCuadrado(int(w), int(h)) :
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

def find_squares(imgOrig):
    img = cv2.GaussianBlur(imgOrig, (5, 5), 0)
    squares = []
    
    for gray in cv2.split(img):
        
        for thrs in xrange(0, 255, 20):
            if thrs == 0:
                bin = cv2.Canny(gray, 25, 350, apertureSize=3)
                kernel = np.ones((3,3), np.uint8)
                bin = cv2.dilate(bin, kernel)
                #bin = cv2.erode(bin, kernel)
                #Imagen(bin).show()
            else:
                retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
                #Imagen(bin).show()
                
            contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            
            for cnt in contours:
                #contornos cerrados 
                cnt_len = cv2.arcLength(cnt, True)
                epsilon = 0.025*cv2.arcLength(cnt,True)
                cnt = cv2.approxPolyDP(cnt, epsilon, True)
              
                if len(cnt) == 4 and cv2.contourArea(cnt) > 50 and cv2.contourArea(cnt) <1700 and cv2.isContourConvex(cnt) :
                    cnt = cnt.reshape(-1, 2)
                    max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
                    if (max_cos < 0.5 and colorCorrecto(imgOrig,cnt) and proporcionesCorrectas(cv2.minAreaRect(cnt))): 
                        squares.append(cnt)
    return squares

if __name__ == '__main__':
    from glob import glob
    for elem in os.listdir("../Pictogramas"):  
        img = cv2.imread('../Pictogramas/'+elem)
        squares = find_squares(img)
        Imagen(img).show()
        if len(squares) == 0 :
          squares=ls.find_squares(img)
        if elem == "picto5.jpg":
          squares=squares+ls.find_badSquare(img)
        cv2.drawContours( img, squares, -1, (0, 255, 0), 3 )
        Imagen(img).show()
