function B = convolucionar3(inputImage, filtro);
%convoluciona imagen y filtro
    [yImagen xImagen] = size(inputImage);
    [yFiltro xFiltro] = size(filtro);
%1.-invertimos filtro
    ortlif = rot90(filtro, 2);
%2.-obtenemos el centro del fitro 
    center = floor((size(ortlif)+1)/2);
    left = center(2) - 1;
    right = xFiltro - center(2);
    top = center(1) - 1;
    bottom = yFiltro - center(1);
%3.-Creamos base para la imagen y copiamos
    Rep = zeros(yImagen + top + bottom, xImagen + left + right);
    for x = 1 + top : yImagen + top
        for y = 1 + left : xImagen + left
            Rep(x,y) = inputImage(x - top, y - left);
        end
    end
%4.- Creamos imagen de salida
    B = zeros(yImagen , xImagen);
%5.- recorremos altura imagen y anchura
    for x = 1 : yImagen
        for y = 1 : xImagen
%6.- recorremos en porciones de filtro y acumulamos posiciones
            for i = 1 : yFiltro
                for j = 1 : xFiltro
                    q = x - 1;
                    w = y -1;
%7.- acumulamos reiteradamente
                    B(x, y) = B(x, y) + (Rep(i + q, j + w) * ortlif(i, j));
                end
            end
        end
    end
