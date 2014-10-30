function [ paso3 ] = supresionNoMaxima( or,mag )
%SUPRESIONNOMAXIMA dada matriz orientaciones y magnitudes clasificamos los bordes // resaltamos los que son bordes 
  paso3 = zeros(size(mag));
   for i=2:(size(mag,1)-1)
     for j=2:(size(mag,2)-1)
         if(mag(i,j)>0)
            switch (or(i,j))
                case 2 %0
                     if(mag(i,j)>mag(i,j-1) && mag(i,j)>mag(i,j+1))
                        paso3(i,j)=mag(i,j);
                     end
                case 3 %45
                     if(mag(i,j)>mag(i-1,j+1) && mag(i,j)>mag(i+1,j-1))
                         paso3(i,j)=mag(i,j);
                     end
                case 4 %90
                     if(mag(i,j)>mag(i-1,j) && mag(i,j)>mag(i+1,j))
                         paso3(i,j)=mag(i,j);
                     end
                case 5 %135
                     if(mag(i,j)>=mag(i-1,j-1) && mag(i,j)>=mag(i+1,j+1))
                         paso3(i,j)=mag(i,j);
                     end
            end
         end
     end
   end
end

