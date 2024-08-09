print("--- Part 1 ---")
numberlist=[]
x,sum = True,0
while x:
    number = int(input("How many integer (5-10): "))
    if (number>=5 and number<=10):
        x = False
    else :
        print("Must be 5 to 10")


        
print("\n--- Part 2 ---")
for i in range(number):
    number1 = int(input("Number %d = "%(i+1)))
    numberlist.append(number1)
print("number =",numberlist)


print("\n--- Part 3 ---")
for i in range(number):
    print("Number %d ==> %d"%(i+1,numberlist[i]))
    if (numberlist[i]%2 == 0):
        print("\t%d is added."%numberlist[i])
        sum += numberlist[i]
    else :
        print("\t%d is an odd number and it is not added."%numberlist[i])
print("Total sum of even numbers is %d."%sum)