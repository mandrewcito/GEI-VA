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
