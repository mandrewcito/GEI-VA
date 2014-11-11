import cv2
import numpy as np
import constantes as c
class Imagen:
  def __init__(self,imagen,name):
    if type(imagen) ==str:
      self.imagen=cv2.imread(c.test+"/"+imagen,0)
    else :
      if type(imagen)==np.ndarray:
        self.imagen=imagen
    self.name=name

  def size(self):
    #Total number of pixels is accessed
    return  self.imagen.size

  def show(self):
    cv2.namedWindow(self.name, cv2.CV_WINDOW_AUTOSIZE)
    cv2.startWindowThread()
    cv2.imshow(self.name,self.imagen)
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()

  def type(self):
    return self.imagen.dtype

  def shape(self):
    #returns a tuple of number of rows, columns and channels 
    return self.imagen.shape

  def averageBlur(self,kernelx,kernely):
    #suaviza una imagen con un kernel dados x,y del kernel
    img=cv2.blur(self.imagen,(kernelx,kernely))
    return Imagen(img,self.name+"averageBlur"+"x-"+str(kernelx)+",y-"+str(kernely))

  def gaussianBlur(self,kernelx,kernely,sigma):
     #suaviza una imagen con un kernel dados x,y del kernel y sigma 
    img=cv2.GaussianBlur(self.imagen,(kernelx,kernely),sigma)
    return Imagen(img,self.name+"gaussianBlur"+"x-"+str(kernelx)+",y-"+str(kernely)+"sigma-"+str(sigma))

