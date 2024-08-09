while 1:
    n = int(input("How many number (5-10): "))
    if n>=5 and n<=10:
        break
    else:
        print("Invalid NUmber!!!")
nlist = []
for i in range(n):
    n1 = int(input(f"Number {i+1}: "))
    nlist.append(n1)
print(f"Original List: {nlist}")

for j in range(n-1):
    key = j
    for k in range(j+1,n):
        if nlist[key] > nlist[k]:
            key = k
    temp = nlist[j]
    nlist[j] = nlist[key]
    nlist[key] = temp
    print(f"After Round {j+1}: {nlist}")
print(f"Sorted List: {nlist}")