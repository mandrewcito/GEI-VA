function outputImage = medianFilter(inputImage, filterSize)
%MEDIANFILTER filtro de mediana
    if(filterSize < 3)
        error('El tamano del filtro tiene que ser mayor o igual que 3');
    elseif(mod(filterSize, 2) == 0)
        error('El tamano del filtro tiene que ser un numero impar');
    elseif(filterSize ~= fix(filterSize))
        error('El tamano del filtro tiene que ser un numero entero');
    end
    
    altoImagen = size(inputImage, 1);
    anchoImagen = size(inputImage, 2);                    
    tamBorde = fix(filterSize/2);
    tamExtra = tamBorde * 2;
%1.- Creamos Base para imagen con (-1) en los bordes y copiamos la imagen dentro
    imagen = ones(size(inputImage, 1)+tamExtra, size(inputImage, 2)+tamExtra, size(inputImage, 3))*(-1);
    imagen((tamBorde+1):altoImagen+tamBorde, (tamBorde+1):anchoImagen+tamBorde, :) = normalizarImagen(inputImage);
%2.- Preparamos la imagen de salida
    outputImage = zeros(size(inputImage));
       
%3.- recorremos las capas de la imagen (color)
    for capa = 1:size(inputImage, 3)
%4.- recorremos eje y
        for i = (tamBorde+1):(altoImagen + tamBorde)
%5.- recorremos eje x
            for j = (tamBorde+1):(anchoImagen + tamBorde)
%6.- obtengo la matriz de valores y ordeno los distintos de -1
                valoresBloque = imagen(i-tamBorde:i+tamBorde, j-tamBorde:j+tamBorde);
                valoresBloqueValidos = sort(valoresBloque(valoresBloque ~= -1));
%6.1.- Si es numero impar hay solo un candidato a mediana
                if(mod(length(valoresBloqueValidos), 2) == 1)
                    outputImage(i-tamBorde, j-tamBorde, capa) = valoresBloqueValidos(ceil(length(valoresBloqueValidos)/2));
                else
%6.2 - Si el numero es par promediamos los dos candidatos a mediana
                    outputImage(i-tamBorde, j-tamBorde, capa) = ...
                        ( valoresBloqueValidos(length(valoresBloqueValidos)/2) + ...
                          valoresBloqueValidos(length(valoresBloqueValidos)/2 + 1) )/2; 
                end
            end             
        end
    end
%6.3.- Devolvemos en rango [0-255]                
    outputImage = uint8(outputImage*255);
end
