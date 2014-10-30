function outputImage = closing(inputImage, strElType, strElSize)
% Dilate + erode
    outputImage = erode(dilate(inputImage, strElType, strElSize), strElType, strElSize);
end
