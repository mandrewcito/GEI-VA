#/usr/bin/env python
# -*- cofing: utf-8 -*-
import os
from imagen import Imagen
from plot import Plot
import constantes as c
import facedetect as f

def main():
  imgSrc=os.listdir(c.test)
  imagenes=[]
  total=0
  detectadas=0
  for e in imgSrc:
    total+=1
    im,todo=f.detectFace(Imagen(e).imagen,e)
    if todo:
      detectadas+=1
    tmp=Imagen(im,name=e)
    imagenes.append(tmp)
  plt=Plot()
  tmp=[]
  print "total caras = "+str(total)+" todo detectado = "+str(detectadas)
  for e in imagenes:
    tmp.append((e.imagen,e.name))
  plt.show(tmp,5)

if __name__ == "__main__":
  main()
