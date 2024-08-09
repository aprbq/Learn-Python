#B6534707
import math, cmath
(y_1,y_2) = 50,0
za = 4j
zb = 2-4j
zc = 8
zx = za+zb+zc
z1 = (za*zb)/zx
z2 = (za*za)/zx
z3 = (zc*zb)/zx

z = (12+z1)+(((z2-3j)+(z3+6j+8))/((z2-3j)*(z3+6j+8)))
(z_1,z_2)=cmath.polar(z)
z_2 = math.degrees(z_2)
(I1,I2) = (y_1/z_1),(y_2-z_2)
print("I = ",I1,"^",I2," A")