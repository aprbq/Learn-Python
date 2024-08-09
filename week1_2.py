rows = int(input("Width: "))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if (j==1 or i==rows or (j==i)):
            print(i,end="")
        else:
            print(" ",end="")
    print()