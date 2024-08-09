x = True
wordlist = {}
while x:
    number = int(input("How many word? (3-5): "))
    if number>5 or number<3:
        print("Invalid number!!!")
    else:
        x = False
for i in range(0,number):
    word = input("Word %d: "%(i+1))
    wordlist[word] = len(word)
print("Key:",wordlist.keys())
print("Value:",max(wordlist.values()))
print("Data in the dictionary:",wordlist)