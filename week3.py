s = input("Enter a string: ")
print("Original string =",s)
print("Using function sorted():",sorted(s))
s1 = list(s)
print("Convert string to list",s1)
print("\nUsing Bubble Sort")
for i in range(len(s1)-1):
    for j in range(len(s1)-i-1):
        if s1[j] > s1[j+1]:
            temp = s1[j]
            s1[j] = s1[j+1]
            s1[j+1] = temp
    print(f"After Round {i+1}: {s1}")
print(f"Sorted List: {s1}")
