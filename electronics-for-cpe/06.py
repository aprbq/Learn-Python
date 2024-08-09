#B6534707
import math, cmath
W = 10
XL = 5j
Xc = -2j
(x_c1,x_c2) = cmath.polar (Xc) 
x_c2 = math.degrees(x_c2) 
Rn = (10*XL)/(10+XL)
R = Rn+Xc
(R1,R2) = cmath.polar(R)
R2 = math.degrees (R2)
(V1,V2) = 10,75
(Z1,Z2) = R1,R2
(I1,I2) = V1/Z1, V2-Z2
(Vo1, Vo2) =I1*x_c1,I2+x_c2
print("V(t) = ", Vo1, "cos(",W,"t", Vo2,")")