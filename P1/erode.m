function outputImage = erode (inputImage, strElType, strElSize)
%ERODE operador morfologico que elimina ruido
    if(strElSize < 3)
        error('tamano filtro < 3');
    elseif(mod(strElSize, 2) == 0)
        error('tamano elemento par');
    elseif(strElSize ~= fix(strElSize))
        error('tamano elemento no entero');
    end
%1.-Creamos el elemento de erosion
    [elementoErosion,tamBordeAncho,tamBordeAlto]=createEE(strElType, strElSize);
    altoImagen = size(inputImage, 1);
    anchoImagen = size(inputImage, 2);                        
        
%2.- Creamos imagen base (+) para guardar el resultado y copiamos   
    imagen = zeros(size(inputImage, 1)+tamBordeAlto*2, size(inputImage, 2)+tamBordeAncho*2, size(inputImage, 3));
    imagen(tamBordeAlto+(1:altoImagen), tamBordeAncho+(1:anchoImagen), :) = inputImage;
    
%3.- Preparamos imagen salida
    outputImage = zeros(size(inputImage));
       
%4.- Recorremos capas imagen (color)
    for capa = 1:size(inputImage, 3)
%5.- Recorremos imagen 
        for i = tamBordeAlto + (1:altoImagen)
            for j = tamBordeAncho + (1:anchoImagen)
                
%6.- Guardo los necesarios
                valoresBloque = imagen(i-tamBordeAlto:i+tamBordeAlto, j-tamBordeAncho:j+tamBordeAncho);
%7.- Aplicamos elemento erosion
                bloqueErosionado = valoresBloque.*elementoErosion;
%8.- Guardamos el minimo del bloque (solo todos 255, entonces 255)
                outputImage(i-tamBordeAlto, j-tamBordeAncho,capa) = min(bloqueErosionado(:));
            end             
        end
    end    
%9.- Devolvemos la imagen    
    outputImage = uint8(outputImage);
end
