#/usr/bin/env python
# -*- cofing: utf-8 -*-

import os
from imagen import Imagen
from plot import Plot
import constantes as c
import facedetect as f

def main():
  #las imagenes estan bien y opencv las muestra bien pero plot no :S
  imgSrc=os.listdir(c.test)
  imagenes=[]
  for e in imgSrc:
    im,recs=f.detectFace(Imagen(e).imagen)
    tmp=Imagen(im)
    imagenes.append(tmp)
  plt=Plot()
  tmp=[]
  for e in imagenes:
    tmp.append(e.imagen)
  plt.show(tmp,5)

if __name__ == "__main__":
  main()
