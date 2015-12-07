import cv2
import numpy as np
import constantes as c
class Imagen:
  def __init__(self,imagen,name=""):
    self.name=name
    self.src = name
    if type(imagen) == str:
      self.src = c.test+"/"+imagen+".jpg"
      self.imagen=cv2.imread(self.src)
    elif type(imagen)==np.ndarray:
        self.imagen=imagen
    if name == "" and type(imagen) == str:
      self.name=imagen

  def size(self):
    #Total number of pixels is accessed
    return  self.imagen.size

  def gray(self):
    return Imagen(cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY),name=self.name)

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

  def averageFilter(self,kernelx,kernely):
    #suaviza una imagen con un kernel dados x,y del kernel
    img=cv2.blur(self.imagen,(kernelx,kernely))
    return Imagen(img,self.name+"averageBlur"+"x-"+str(kernelx)+",y-"+str(kernely))

  def gaussianFilter(self,kernelx,kernely,sigma):
     #suaviza una imagen con un kernel dados x,y del kernel y sigma 
    img=cv2.GaussianBlur(self.imagen,(kernelx,kernely),sigma)
    return Imagen(img,self.name+"gaussianBlur"+"x-"+str(kernelx)+",y-"+str(kernely)+"sigma-"+str(sigma))

  def medianFilter(self,kernelSize):
    img = cv2.medianBlur(self.imagen,kernelSize)
    return Imagen(img,self.name+"medianBlur"+"KernelSize--"+str(kernelSize))

  def bilateralFilter(self,size,x,y):
    img=cv2.bilateralFilter(self.imagen,size,x,y)
    return Imagen(img,self.name+"bilateralBlur"+"KernelSize--"+str(size))

  def blur(self,tipo):
    #suavizado
    if tipo=="average":
      return self.averageFilter(5,5)
    if tipo=="gaussian":
      return self.gaussianFilter(5,5,0)
    if tipo=="median":
      return self.medianFilter(5)
    if tipo=="bilateral":
      return self.bilateralFilter(9,75,75)
    print "el tipo tiene que ser : average | gaussian | median | bilateral" 

  def cornerHarris(self):
    gray = cv2.cvtColor(self.imagen,cv2.COLOR_BGR2GRAY)
    gray=np.float32(gray)
    dst=cv2.cornerHarris(gray,2,3,0.04)
    dst = cv2.dilate(dst,None)
    img=self.imagen
    img[dst>0.01*dst.max()]=[0,0,255]
    return Imagen(img,self.name+"cornerHarris")

  def simpleThresholding(self,rango,tipo,otsu):
    #tipo:binary |binaryInv | trunc | toZero | toZeroInv
    pass

  def adaptiveThresholding(self,rango,tipo,otsu):
    #tipo : mean |gaussian
    pass

  def Thresholding(self,tipo):
    #umbralizado de imagenes
    if tipo=="simple":
      return self.simpleThresholding((100,255),"binary",True)
    if tipo=="Adaptive":
      return self.adaptiveThresholding((100,255),"gaussian",False)
    print "tipo binary o gaussian , true or false on otsu" 


