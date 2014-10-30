function [ outputImage ] = normalizarImagen( inputImage )
%NORMALIZARIMAGEN Normalizamos la imagen    
    outputImage = double(inputImage)/255;
end
