#!/usr/bin/env python
import cv2
from find_obj import filter_matches,explore_match
import constantes as c 
import recortar as r
from imagen import Imagen
import filtrar as flt
import facedetect as f
import sys
args = sys.argv[1:]
sujeto1=args[0]
sujeto2=args[1]
im1=c.test+"/image-"+sujeto1+".jpg"
im2=c.test+"/image-"+sujeto2+".jpg"
img1 = cv2.imread(im1,0) # queryImage
img2 = cv2.imread(im2,0) # trainImage
# Initiate SIFT detector
orb = cv2.ORB()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING)#, crossCheck=True)
#filtramos los kp por la zona de la cara para las dos imagenes 
a,b,c= f.detectFace(cv2.imread(im1),"im1")
region1=c[0][0]
a,b,c= f.detectFace(cv2.imread(im2),"im2")
region2=c[0][0]
matches = bf.knnMatch(des1, trainDescriptors = des2, k = 2)
p1, p2, kp_pairs = filter_matches(kp1, kp2, matches)
print len(kp_pairs)
kp_pairs=flt.filtrarKP(kp_pairs,region1,region2)
print len(kp_pairs)
kp_pairs=flt.filtrarKPCuadrantes(kp_pairs,region1,region2)
print len(kp_pairs)
explore_match('find_obj', img1,img2,kp_pairs)#cv2 shows image
if len(kp_pairs)>15:
  print True
else:
  print False
cv2.waitKey()
cv2.destroyAllWindows()
