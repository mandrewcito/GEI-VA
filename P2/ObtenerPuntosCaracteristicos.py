import cv2
import numpy as np
from imagen import Imagen

def dibujarPuntos(imagen):
  orb=cv2.ORB()
  keypoints=orb.detect(imagen)
  cv2.drawKeypoints(imagen,keypoints,imagen)
  return imagen,keypoints
