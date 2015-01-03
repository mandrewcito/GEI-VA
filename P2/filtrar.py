def filtrarKP(kp,region1,region2):
  newKP=[]
  for puntos in kp:
    if esta(puntos[0].pt,region1,puntos[1].pt,region2):
      newKP.append(puntos)
  return newKP

def esta(coord1,region1,coord2,region2):
  ptx,pty=coord1
  [x1r,y1r,x2r,y2r]=region1
  region=False
  if int(ptx)>x1r and int(ptx)<x2r and int(pty)>y1r and int(pty)<y2r:
    region=True
  ptx,pty=coord2
  [x1r,y1r,x2r,y2r]=region2
  if region:
      if int(ptx)>x1r and int(ptx)<x2r and int(pty)>y1r and int(pty)<y2r:
        return True
  return False

def filtrarKPCuadrantes(kp,region1,region2):
  newKP=[]
  for puntos in kp:
    if estaCuadrante(puntos[0].pt,region1,puntos[1].pt,region2):
      newKP.append(puntos)
  return newKP

def estaCuadrante(coord1,region1,coord2,region2):
  pt1x,pt1y=coord1
  [x1r,y1r,x2r,y2r]=region1
  mediox1=x1r+((x2r-x1r)/2)
  medioy1=y1r+((y2r-y1r)/2)
  pt2x,pt2y=coord2
  [x1r,y1r,x2r,y2r]=region2
  mediox2=x2r+((x2r-x1r)/2)
  medioy2=y2r+((y2r-y1r)/2)
  #designamos cuadrante 00 01 10 y 11 de iz a derecha y arriba a abajo
  #cuadrante 00
  if pt1x < mediox1 and pt1y < medioy1 and pt2x < mediox2 and pt2y < medioy2 :
    return True
  #cuadrante 01
  if pt1x > mediox1 and pt1y < medioy1 and pt2x > mediox2 and pt2y < medioy2 :
    return True
  #cuadrante 10
  if pt1x < mediox1 and pt1y > medioy1 and pt2x < mediox2 and pt2y > medioy2 :
    return True
  #cuadrante 11
  if pt1x > mediox1 and pt1y > medioy1 and pt2x > mediox2 and pt2y > medioy2 :
    return True
  return False

def filtrarKPCaracteristicas(kp_pairs,c1,c2):
  cara1=c1[0][0]
  xstart1=cara1[0]
  ystart1=cara1[1]
  cara2=c2[0][0]
  xstart2=cara2[0]
  ystart2=cara2[1]
  newKP=[]
  for puntos in kp_pairs:
    boca1=c1[1][0]
    region1=[boca1[1]+xstart1,boca1[0]+ystart1,boca1[3]+xstart1,boca1[2]+ystart1]
    boca2=c2[1][0]
    region2=[boca2[1]+xstart2,boca2[0]+ystart2,boca2[3]+xstart2,boca2[2]+ystart2]
    if esta(puntos[0].pt,region1,puntos[1].pt,region2):
      newKP.append(puntos)
      continue
    nariz1=c1[2][0]
    region1=[nariz1[1]+xstart1,nariz1[0]+ystart1,nariz1[3]+xstart1,nariz1[2]+ystart1]
    nariz2=c2[2][0]
    region2=[nariz2[1]+xstart2,nariz2[0]+ystart2,nariz2[3]+xstart2,nariz2[2]+ystart2]
    if esta(puntos[0].pt,region1,puntos[1].pt,region2):
      newKP.append(puntos)
      continue
    ojo11=c1[3][0]
    region1=[ojo11[1]+xstart1,ojo11[0]+ystart1,ojo11[3]+xstart1,ojo11[2]+ystart1]
    ojo12=c1[3][1]
    region2=[ojo12[1]+xstart2,ojo12[0]+ystart2,ojo12[3]+xstart2,ojo12[2]+ystart2]
    if esta(puntos[0].pt,region1,puntos[1].pt,region2):
      newKP.append(puntos)
      continue
    ojo21=c2[3][0]
    region1=[ojo21[0]+xstart1,ojo21[1]+ystart1,ojo21[2]+xstart1,ojo21[3]+ystart1]
    ojo22=c2[3][1]
    region2=[ojo22[0]+xstart2,ojo22[1]+ystart2,ojo22[2]+xstart2,ojo22[3]+ystart2]
    if esta(puntos[0].pt,region1,puntos[1].pt,region2):
      newKP.append(puntos)
      continue
  print len(newKP)
  return newKP
