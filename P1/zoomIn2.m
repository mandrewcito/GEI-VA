function [outputImage] = zoomIn2( inputImage , mode)
%ZOOMIN2 zoom de imagen mode=’bilinear’ | ’neighbor’
image=double(inputImage);
%se utilizan los 4 px mas cercanos
if (strcmp(mode,'neighbor')==1),
        imagenAmpliada=zeros(size(image)*2);
        imagenAmpliada(1:2:size(imagenAmpliada, 1), 1:2:size(imagenAmpliada, 2)) = image;
        imagenAmpliada(1:2:size(imagenAmpliada, 1), 2:2:size(imagenAmpliada, 2)) = image;
        imagenAmpliada(2:2:size(imagenAmpliada, 1), 1:2:size(imagenAmpliada, 2)) = image;
        imagenAmpliada(2:2:size(imagenAmpliada, 1), 2:2:size(imagenAmpliada, 2)) = image;   
end

if (strcmp(mode,'bilinear')==1),      
%2.2.1 copiamos e interpolamos verticalmente
        imagenAmpliadaFilas = zeros(size(image, 1)*2, size(image, 2)); 
        imagenAmpliadaFilas(1:2:size(imagenAmpliadaFilas, 1), :) = image;
        imagenAmpliadaFilas(2:2:size(imagenAmpliadaFilas, 1)-1, :) = (image(1:size(image, 1)-1, :) + image(2:size(image, 1), :))/2;
%2.2.2 copiamos la anterior e interpolamos horizontalmente
        imagenAmpliada = zeros(size(image)*2);
        imagenAmpliada(:, 1:2:size(imagenAmpliada, 2)) = imagenAmpliadaFilas;
        imagenAmpliada(:, 2:2:size(imagenAmpliada, 2)-1) = (imagenAmpliadaFilas(:, 1:size(imagenAmpliadaFilas, 2)-1) + imagenAmpliadaFilas(:, 2:size(imagenAmpliadaFilas, 2)))/2;
end
outputImage=uint8(imagenAmpliada);

end
