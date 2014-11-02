function [outImg] = main(imgsrc,option,args,type)
%MAIN programa principal
mostrarImg=true;
image=cargarImagen(imgsrc);
if mostrarImg,
figure
imshow(image);
end
switch(option)
    case 'histStretch'
        minValue=args(1);
        maxValue=args(2);
        outImg=histStretch(image,minValue,maxValue);
    
    case 'zoomIn2'
        outImg=zoomIn2(image,args);
    
    case 'highBoost'
        filterSize=args(1);
        A=args(2);
        outImg=highBoost(image,filterSize,A);
    
    case 'medianFilter'
        filterSize=args(1);
        outImg=medianFilter(image,filterSize);
    
    case {'erode','dilate','opening','closing'}
        strElType=type;
        strElSyze=args(1);
        fun=str2func(option);
        outImg=fun(image,strElType,strElSyze);
        
    case 'edgeCanny'
        n=args(1);
        sigma=args(2);
        tlow=args(1);
        thigh=args(3);
        edgeDetector=type;
        outImg=edgeCanny(image,n,sigma,tlow,thigh,edgeDetector);
        
    case 'cornerSusan'
        radius=args(1);
        threshold=args(2);
        coefG=args(3);
        outImg=cornerSusan(image,radius,threshold,coefG);
    otherwise 
        error('La función indicada no es valida');  
end
if mostrarImg,
    figure
    imshow(outImg);
end
end
