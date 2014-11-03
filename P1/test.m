function output =test(option)
switch(option)
    case 'histStretch'
        output =main('imagenes/chica.png',option,[0 200]);
    
    case 'zoomIn2'
     % output =  main('imagenes/zoom.jpeg',option,'neighbor');
      output =  main('imagenes/zoom.jpeg',option,'bilinear');
    
    case 'highBoost'
      output =  main('imagenes/zoom.jpeg',option,[3 2]);
    
    case 'medianFilter'
       output = main('imagenes/zoom.jpeg',option,[3]);
    
    case {'erode','dilate','opening','closing'}
      output = main('imagenes/erode-dilate.jpg',option,[7],'square');
      %output =  main('imagenes/erode-dilate.jpg',option,[7],'cross');

        
    case 'edgeCanny'
       output =main('images/cat.gif',option,[5 2 10 20],'Prewitt');
        
    case 'cornerSusan'
       output = main('imagenes/susan.png',option,[3 40 2/4]);
    otherwise 
        error('La función indicada no es valida');  
end
end
