#B6534707
import math, cmath 
X1 = 0 + 20j
Xc = 0 - 25j
R = 60
Y = cmath.rect(20, math.radians(-15)) 
Z = cmath.rect(100, math.radians(90))
Result = X1*Xc/(X1+Xc)
ResultX = R + Result
(Result_R, Result_RadR) = cmath.polar(ResultX) 
(Result_Y, Result_RadY)= cmath.polar(Y)
(Result_Z, Result_RadZ) = cmath.polar(Z)
Result_DegR = math.degrees(Result_RadR)
Result_DegY = math.degrees(Result_RadY)
Result_DegZ = math.degrees(Result_RadZ)
V = (Result_Z*Result_Y)/Result_R
Vdree = (Result_DegZ+Result_DegY) - Result_DegR 
print("v(t) = %0.2fCos(4t+%0.2f)" % ( V, Vdree))