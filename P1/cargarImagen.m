function [ image ] = cargarImagen( imgsrc)
%carga una img dada una ruta y la pasa a escala de grises
f=imread(imgsrc);
if size(f,3)==3,
image=rgb2gray(f);
elseif size(f,3)==1,
image=f;
end
end
