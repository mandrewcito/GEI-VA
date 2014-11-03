function output =test(option)
switch(option)
    case 'histStretch'
        main('imagenes/chica.png',option,[0 200]);
    
    case 'zoomIn2'
        main('imagenes/zoom.jpeg',option,'neighbor');
        main('imagenes/zoom.jpeg',option,'bilinear');
    
    case 'highBoost'
        main('imagenes/zoom.jpeg',option,[3 2]);
    
    case 'medianFilter'
        main('imagenes/zoom.jpeg',option,[3]);
    
    case {'erode','dilate','opening','closing'}
        main('imagenes/erode-dilate.jpg',option,[7],'square');
        main('imagenes/erode-dilate.jpg',option,[7],'cross');

        
    case 'edgeCanny'
       main('imagenes/chica.png',option,[5 2 10 20],'Prewitt');
        
    case 'cornerSusan'
        main('imagenes/susan.png',option,[3 40 2/4]);
    otherwise 
        error('La función indicada no es valida');  
end
end
