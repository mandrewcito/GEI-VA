%A factor de amplificacion, cuanto mayor sea mayor info de la img original
%se mantinene 
function [ outputImage ] = highBoost( inputImage,filterSize,A)
%HIGHBOOST algoritmo de realce 
if(filterSize < 3),
   error('tamano < 3');
elseif(mod(filterSize, 2) == 0),
   error('tamano filtro par');
elseif(filterSize ~= fix(filterSize))
   error('tamano filtro no entero');    
end
if(A < 1)
  error('Valor de a < 1');
end
%Puede calcularse mediante máscaras de
%convolución
%Si A = 0 → Laplaciano
%Si A < 0 → Bordes
%%%%%%Si A >= 1 → Realce%%%%%%
image=double(inputImage)/255;
%crear filtro
filtro=createFilter(filterSize,A);
%Convolucionamos la imagen con el filtro
%resultadoFiltro=convn(image,filtro);
resultadoFiltro = convolucionar(image, filtro);
%Ghb(x,y)=(A-1)f(x,y)+(f(x,y)-fsmooth(x,y))
imagenRealzada =(A-1)*image + resultadoFiltro;
%Le agregamos a la img realzada el filtro
imagenRealzada = imagenRealzada + abs(min(resultadoFiltro(:)));
%Devolvemos la imagen en rango 
outputImage = uint8((imagenRealzada/max(imagenRealzada(:)))*255);  
end
