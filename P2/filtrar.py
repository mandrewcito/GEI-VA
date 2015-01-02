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
