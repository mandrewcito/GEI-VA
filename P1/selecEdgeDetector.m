function [ mascara_x,mascara_y ] = selecEdgeDetector( inputEdgeDetector )
%SELECEDGEDETECTOR edge detector on canny edge dectector
switch(inputEdgeDetector)
    case'Sobel'
        Gx=[-1 -2 -1; 0 0 0; 1 2 1];
        Gy=[-1 0 1; -2 0 2; -1 0 1];
    case'Prewitt'
        Gx=[-1 -1 -1; 0 0 0; 1 1 1];
        Gy=[-1 0 1; -1 0 1; -1 0 1];
    case'Roberts'
        Gx=[-1 0; 0 1];
        Gy=[0 -1; 1 0];
    otherwise
        error(' introduzca un detector valido Sobel / Prewitt / Roberts');
end
mascara_x=transpose(Gx);
mascara_y=transpose(Gy);
end

