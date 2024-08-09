print("--- Part 1 ---")
number1 = int(input("How many integer (5-10): "))
while number1<5 or number1>10:
    print("Must be to 5 - 10")
    number1 = int(input("How many integer (5-10): "))
    
print("\n--- Part 2 ---")
number3 = []
for j in range(number1):
    number2 = int(input(f"Number {j+1}: "))
    number3.append(number2)
print(f"number = {number3}")

print("\n--- Part 3 ---")
big,maxb,small,maxs,minb,mins = 0,0,0,0,9,9
for k in range(len(number3)):
    print(f"Number {k+1} ==> {number3[k]}")
    if number3[k]>=5:
        print(f"      {number3[k]} is a big number.")
        big += 1
        if number3[k]>maxb:
            maxb = number3[k]
        if number3[k]<minb:
            minb = number3[k]
    else :
        print(f"      {number3[k]} is a small number.")
        small += 1
        if number3[k]>maxs:
            maxs = number3[k]
        if number3[k]<mins:
            mins = number3[k]
if big>0:
    print(f"Big number have: {big}")
    print(f"{maxb} is a max in big number")
    print(f"{minb} is a min in big number")
else:
    print("Dont have big number")
if small>0:
    print(f"small number have: {small}")
    print(f"{maxs} is a max in small number")
    print(f"{mins} is a min in small number")
else:
    print("Dont have small number")