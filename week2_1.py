s = 'ANIMALS'
index = -1
j = -1
k = input("Enter a character to be searched: ")
for i in range(len(s)):
    c = s[i]
    j += 1
    if c == k:
        index = j
        break
if index == -1:
    print(f"Cannot find '{k}'")
else:
    print(f"Foubd '{k}' at index {index}")