function [elementoEstructurante,tamBordeAncho,tamBordeAlto] = createEE(strElType,strElSize)
%CREATEEE Creamos elemento estructurante con el tipo y tamaño indicados,devuelve elemento y dimensiones
    switch(strElType)
        case 'square'
            elementoEstructurante = ones(strElSize);
            tamBordeAncho = fix(strElSize/2);
            tamBordeAlto = fix(strElSize/2);
        case 'cross'
            elementoEstructurante = inf(strElSize); %se usa inf -> al buscar min sea correcto
            elementoEstructurante(ceil(strElSize/2), :) = 1;
            elementoEstructurante(:, ceil(strElSize/2)) = 1;
            tamBordeAncho = fix(strElSize/2);
            tamBordeAlto = fix(strElSize/2);
        case 'lineh'
            elementoEstructurante = ones(1,strElSize);
            tamBordeAncho = fix(strElSize/2);
            tamBordeAlto = 0;            
        case 'linev'
            elementoEstructurante = ones(strElSize,1);
            tamBordeAncho = 0;
            tamBordeAlto = fix(strElSize/2);            
        otherwise 
            error('La forma del elemento de erosion indicada no es valida');            
    end
end

