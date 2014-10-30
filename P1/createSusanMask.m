function [ susanMask,g] = createSusanMask(radius,coefG)
%CREATESUSANMASK Crea mascara circular para detector de esquinas susan
diametro=(2*radius)+1;
susanMask=zeros(diametro,diametro);
centro=ceil(diametro/2);
[imax,jmax]=size(susanMask);
n=0;
for i=1:imax,
    for j=1:jmax,
        c1=abs(centro-i);
        c2=abs(centro-j);
        %si esta en el area de la circunferencia ->1
        if (c2^2+c1^2<=radius^2+1)
            n=n+1;
            susanMask(i,j)=1;
        end
    end
end
g=ceil(n*coefG);%tambien valdria nnz(mask) -> devuelve el numero de elem que no son 0
end

