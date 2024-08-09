#B6534707
import math, cmath
W = 10
Z1 = 20 + (0-1j)/(W*0.002) 
Z2 = 0+(0-1j)/(W*0.004) 
Z3 = 50+ (+1j)*(W*2)
Result = Z1 +Z2*Z3/(Z2+Z3)
(Result_R, Result_Rad) = cmath.polar(Result) 
Result_Deg = math. degrees (Result_Rad) 
print("x + jy = ", Result)
print("(r,Zeta) = (%.15f,%.15f)"% (Result_R, Result_Deg))