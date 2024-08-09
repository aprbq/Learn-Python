import math, cmath
W = 10
XR = 4
XL = (0+1j)*W*0.2
VS =cmath.rect(5,math.radians(-90))
I = VS/(XR+XL) 
V = I*XL

Result = I
(Result_R,Result_Rad) = cmath.polar(Result) 
Result_Deg = math.degrees(Result_Rad)
print("x + jy = ", Result)
print("(r,Zeta) = (%.15f,%.15f)"% (Result_R,Result_Deg))

Result = V
(Result_R,Result_Rad) = cmath.polar(Result) 
Result_Deg = math.degrees(Result_Rad)
print("x + jy = ",Result)
print("(r,Zeta) = (%.15f,%.15f)"% (Result_R,Result_Deg))