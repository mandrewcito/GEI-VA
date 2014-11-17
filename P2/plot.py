import numpy as np
import cv2
from matplotlib import pyplot as plt

class Plot:
  def __init__(self):
    pass

  def show(self,imageList,rows):
    size = len(imageList)
    if size == 0:
      raise("error lista de imagenes vacia")
    if size%rows==0:
      cols=size/rows
    else:
      cols=size/rows+1
    for n,img in enumerate(imageList):
      image=self.normalize(img[0])
      plt.subplot(rows,cols,n+1),plt.imshow(image),plt.title(img[1])
      plt.xticks([]),plt.yticks([])
    plt.show()

  def normalize(self,vis):
    x,y,canales=vis.shape
    visF=np.zeros((x,y,canales),np.float32)
    b=vis[:,:,0]
    g=vis[:,:,1]
    r=vis[:,:,2]              
    visF[:,:,0]=b/255.0
    visF[:,:,1]=g/255.0
    visF[:,:,2]=r/255.0
    return visF
