function [outputImage] = histStretch( inputImage , gminNorm , gmaxNorm )
%HISTSTRETCH comprime / expande histograma de una imagen
image=(inputImage);
%Gnorm(x,y)=GminNorm+((GmaxNorm-GminNorm)*(g(x,y)-Gmin))/Gmax-Gmin
gmin=min(min(image));
gmax=max(max(image));
gdiff=gmax-gmin;
gNormdiff=gmaxNorm-gminNorm;
tam=size(image);
imgNorm=zeros(tam(1),tam(2));
for x=1:tam(1),
    for y=1:tam(2),
      c=double(image(x,y)-gmin);
      b=gNormdiff*c;
      imgNorm(x,y)=gminNorm+round(b/gdiff);
    end
end
outputImage=uint8(imgNorm);
end
