#/usr/bin/env python
# -*- cofing: utf-8 -*-
import os
from imagen import Imagen
from plot import Plot
import constantes as c
import facedetect as f
import ObtenerPuntosCaracteristicos as opc

def main():
  imgSrc=os.listdir(c.test)
  imagenes=[]
  tmp=[]
  for e in imgSrc:
    img=Imagen(e).imagen
    rects=f.detectCara(img)
    im,key=opc.dibujarPuntos(img)
    tmp.append((im,e))
  plt=Plot()
  plt.show(tmp,5)

if __name__ == "__main__":
  main()
