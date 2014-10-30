function [ paso4 ] = histeresis( paso3,or,tLow,tHigh )
%HISTERESIS recorre orientaciones hasta limite 
  paso4 = zeros(size(paso3));
   for i=1:(size(paso3,1))
     for j=1:(size(paso3,2))
      if(paso3(i,j)>tHigh)
          p=i;
          q=j;
          while(p>0 && q>0 && p<=size(paso3,1) && q<=size(paso3,2) && paso3(p,q)>tLow)
              paso4(p,q)=1;
              switch(or(p,q))
                  case 2 %orientacion 0
                     p=p+1;
                  case 3 %orientacion 45
                     p=p+1;
                     q=q-1;
                  case 4%orientacion 90
                     q=q-1;
                  case 5 %orientacion 135
                     p=p+1;
                     q=q-1;
              end
          end
          p=i;
          q=j;
          while(p>0 && q>0 && p<=size(paso3,1) && q<=size(paso3,2) && paso3(p,q)>tLow)
              paso4(p,q)=1;
              switch (or(p,q))
                  case 2 %orientacion 0
                     p=p-1;
                  case 3 %orientacion 45
                     p=p-1;
                     q=q+1;
                  case 4 %orientacion 90
                     q=q+1;
                  case 5 %orientacion 135
                     p=p-1;
                     q=q+1;
              end
          end
      end
         
     end
   end
end

