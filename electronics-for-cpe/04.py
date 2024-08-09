#B65434707
import math, cmath 
W = 50
Z1 = (0-1j)/(W*0.002) 
Z2 = 3+(0-1j)/(W*0.010)
Z3 = 8+ (0+1j)*(W*0.2)
Result = Z1+ (Z2*Z3/(Z2+Z3))
(Result_R, Result_Rad)= cmath.polar(Result) 
Result_Deg = math. degrees (Result_Rad)
print("x + jy =", Result)
print("(r,Zeta) = (%.15f,%.15f)"% (Result_R, Result_Deg))