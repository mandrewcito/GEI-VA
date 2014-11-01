function outputImage = edgeCanny( inputImage ,n,sigma , tLow , tHigh )
%EDGECANNY detector de bordes canny
debug=0;

  if(debug),
    subplot(3,3,1);
    imshow(inputImage)
    title('Imagen Normal');
  end
% -----------------> PASO 1 MEJORA IMAGEN
  %1.-establecemos umbral y tamaño filtro
  kernelG = gaussianKernel(n,sigma);
  %2.- Convolucionamos con un kernel gausiano
  paso1 = convolucionar(inputImage,kernelG);
  if(debug),
    subplot(3,3,2);
    imshow(uint8(paso1))
    title('Filtro gaussiano');
  end
%3.- Preparamos mascaras y convolucionamos lo anterior
   %mascara_x = [-1 0 1];%sobel
   %mascara_y = [-1; 0; 1];%sobel
   mascara_x = [ 1 0 -1];%prewit
   mascara_y = [-1; 0; 1];%prewit
   res_x = convolucionar(paso1,mascara_x);
   res_y = convolucionar(paso1,mascara_y);
%4.- Obtenemos magnitud y orientacion
    mag=sqrt(res_x.^2+res_y.^2);
    ori = atan(res_y./(res_x+eps));% eps para evitar division entre 0
    or = ((ori>-pi/8 & ori<pi/8).*1 + (ori>=pi/8 & ori<3*pi/8).*2 +(ori>=3*pi/8 | ori<=-3*pi/8).*3 +(ori<=-pi/8 & ori>-3*pi/8).*4) ;
    or = or .* (mag > 0) + 1;
%5.- Tenemos bordes
 % -- rojo 0 -- verde pi/4 
  if debug,
    subplot(3,3,3);
    imshow(mag)
    title('Magnitud Bordes');
    %subplot(3,3,4);
    %image(or)
    %mapa = [0 0 0;1 0 0;0 0 1; 1 1 0.1; 0 1 0];
    %colormap(mapa)
    %title('Orientacion Bordes');
  end
% -----------------> PASO 2 
%6.- Hacemos supresion no Maxima (Orientaciones) (PASO 2 )
  paso3=supresionNoMaxima(or,mag); 
  if debug,
    subplot(3,3,4);
    imshow(paso3)
    title('Supresion no max');
  end
  % -----------------> PASO 3
%7.- hacemos histeresis umbralizacion
   paso4=histeresis(paso3,or,tLow,tHigh);
%invertimos ! 
   ipaso4=ones(size(paso4));
     for i=1:size(paso4,1),
         for j=1:size(paso4,2),
             if paso4(i,j)==1,
                 ipaso4(i,j)=0;
             end
         end
     end
   if debug,
     subplot(3,3,5);
     imshow(paso4);
     title('Histeresis');
     subplot(3,3,6);
     title('negativo canny');
     imshow((ipaso4))
   end
   outputImage = (ipaso4);
end
