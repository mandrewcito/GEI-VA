import facedetect as f
from imagen import Imagen

def cara(imagen):
  gray=imagen.gray().imagen
  rects=f.detectCara(gray)
  a,b,c,d=rects[0]
  img=gray[b:d,a:c]
  return Imagen(img.copy())

