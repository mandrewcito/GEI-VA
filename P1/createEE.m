function [elementoErosion,tamBordeAncho,tamBordeAlto] = createEE(strElType,strElSize)
%CREATEEE Creamos elemento erosion con el tipo y tamaño indicados,devuelve elemento y dimensiones
    switch(strElType)
        case 'square'
            elementoErosion = ones(strElSize);
            tamBordeAncho = fix(strElSize/2);
            tamBordeAlto = fix(strElSize/2);
        case 'cross'
            elementoErosion = inf(strElSize); %se usa inf -> al buscar min sea correcto
            elementoErosion(ceil(strElSize/2), :) = 1;
            elementoErosion(:, ceil(strElSize/2)) = 1;
            tamBordeAncho = fix(strElSize/2);
            tamBordeAlto = fix(strElSize/2);
        case 'lineh'
            elementoErosion = ones(1,strElSize);
            tamBordeAncho = fix(strElSize/2);
            tamBordeAlto = 0;            
        case 'linev'
            elementoErosion = ones(strElSize,1);
            tamBordeAncho = 0;
            tamBordeAlto = fix(strElSize/2);            
        otherwise 
            error('La forma del elemento de erosion indicada no es valida');            
    end
end

