import math

sum = 0
for i in range(0,9):
    sum += (pow(2,i+1)-pow(2,i))
print("Sum =",sum)