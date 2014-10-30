function outputImage = opening(inputImage, strElType, strElSize)
%OPENING Aplicamos una dilatacion a una erosión.
    outputImage = dilate(erode(inputImage, strElType, strElSize), strElType, strElSize);
end

