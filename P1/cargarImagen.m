function [ image ] = cargarImagen( imgsrc)
%carga una img dada una ruta y la pasa a escala de grises
f=imread(imgsrc);
image=rgb2gray(f);
end
