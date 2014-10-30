function [ respuestaBordes ] = obtainLuminance(inputArea,mask,threshold)
%OBTAINLUMINANCE dado un punto devolvemos los el area de luminancia alta (las que coinciden con la mascara y superan el umbral)
[imax,jmax]=size(mask);
sz=size(inputArea,1);
usan = double(ones(sz)*double(inputArea(round(sz/2),round(sz/2))));
similar = (abs(usan-double(inputArea))<threshold);
similar = similar.*mask;
respuestaBordes=sum(similar(:));
end
