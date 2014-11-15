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
      plt.subplot(rows,cols,n+1),plt.imshow(img[0]),plt.title(img[1])
      plt.xticks([]),plt.yticks([])
    plt.show()

