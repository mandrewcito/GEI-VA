function [ filtro ] = createFilter(filterSize,A)
%CREATEFILTER crea filtro para highBoost
    filtro = ones(filterSize)*(-1);
    %9A-1 || A+4  || A+8
    filtro(ceil(filterSize/2), ceil(filterSize/2)) = (9*A -1);
    filtro = filtro/(filterSize*filterSize);
end
