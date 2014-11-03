function output =test(option)
switch(option)
    case 'histStretch'
        main('imagenes/chica.png','histStretch',[0 200]);
    
    case 'zoomIn2'
        main('imagenes/zoom.jpeg','zoomIn2','neighbor');
        main('imagenes/zoom.jpeg','zoomIn2','bilinear');
    
    case 'highBoost'
        main('imagenes/zoom.jpeg','highBoost',[3 2]);
    
    case 'medianFilter'
        main('imagenes/zoom.jpeg','medianFilter',[3]);
    
    case {'erode','dilate','opening','closing'}

        main('imagenes/erode-dilate.jpg','erode',[7],'square');
        main('imagenes/erode-dilate.jpg','dilate',[7],'square');
        main('imagenes/erode-dilate.jpg','opening',[7],'square');
        main('imagenes/erode-dilate.jpg','closing',[7],'square');
        main('imagenes/erode-dilate.jpg','erode',[7],'cross');
        main('imagenes/erode-dilate.jpg','dilate',[7],'cross');
        main('imagenes/erode-dilate.jpg','opening',[7],'cross');
        main('imagenes/erode-dilate.jpg','closing',[7],'cross');
        
    case 'edgeCanny'
       main('imagenes/chica.png','edgeCanny',[5 2 10 20],'Prewitt');
        
    case 'cornerSusan'
        main('imagenes/chess.jpg','cornerSusan',[7 40 2/4]);
    otherwise 
        error('La función indicada no es valida');  
end
end
