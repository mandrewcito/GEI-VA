function kernel = gaussianKernel( n, sigma )
%GAUSSIANKERNEL kernel gausiano para edgeCanny
    if(mod(n, 2) ~= 1)
        error('tamano filtro par');        
    elseif(n < 3)
        error('tamano filtro < 3');
    elseif(n ~= fix(n))
        error('tamaño filtro no entero');
    end

    r = fix(n/2);
    [x y] = meshgrid(-r:r, -r:r);
    kernel = (1/(2*pi*sigma*sigma)) .* exp(-(x.^2 + y.^2)./(2*sigma*sigma));
end
