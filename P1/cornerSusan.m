function [ outputImage] = cornerSusan( inputImage,radius,threshold,coefG )
%CORNERSUSAN resalta esquinas de una imagen
[mask,g]=createSusanMask(radius,coefG);
[imax,jmax]=size(inputImage);
rgb_image=zeros(size(inputImage,1),size(inputImage,2),3);
rgb_image(:,:,1)=inputImage;
rgb_image(:,:,2)=inputImage;
rgb_image(:,:,3)=inputImage;
for i=1:imax,
    for j=1:jmax,
    %comprobamos luminosidad, si es menor que el umbral lo sumamos, si la
    %suma es mayor a 3/4 de g entonces ese punto es un borde
        if(i-radius>0 && j-radius>0 && i+radius<imax && j+radius<jmax),
            suma_luminosidad=obtainLuminance(inputImage(abs(i-radius):abs(i+radius),abs(j-radius):abs(j+radius)),mask,threshold);% dado un punto,mascara y umbral devuelve la luminosidad de el punto c(r,r0)
            if suma_luminosidad<g,
                %respuesta_bordes=g-suma_luminosidad;
                rgb_image(i,j,3)=255;
            end
        end
    end
end
outputImage=uint8(rgb_image);
end
