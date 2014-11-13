from imagen import Imagen
from matplotlib import pyplot as plt

class Plot:
  def __init__(self):
    pass

  def show(self,imageList,rows):
    #TODO hacer el plot en varias lineas por ahora solo lo hace en 1 
    size = len(imageList)
    if size == 0:
      raise("error lista de imagenes vacia")
    if size%rows==0:
      cols=size/rows
    else:
      cols=size/rows+1
    rc=str(rows)+str(cols)
    for n,img in enumerate(imageList):
      num=int(rc+str(n+1))
      plt.subplot(num),plt.imshow(img.imagen),plt.title(img.name)
      plt.xticks([]),plt.yticks([])
    plt.show()

