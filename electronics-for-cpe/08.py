#B6534707
import math, cmath
A = cmath.rect(30,math.radians(0))
B=4j*(-3j)/(4j-3j+8+5j)
C=4j*(8+5j)/(4j-3j+8+5j)
D=-3j*(8+5j)/(4j-3j+8+5j)
E = C+(5-2j)
F = D+10
G = E*F/(E+F)
H = B+G
Result = A/H
(Result_R, Result_Rad)=cmath.polar(Result)
Result_Deg = math.degrees(Result_Rad)
print("x + jy =",Result)
print("(r,Zeta) = (%.15f,%.15f)"% (Result_R, Result_Deg))