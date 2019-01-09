word=input("Enter characters: ")
length=len(word)
for i in range (1, length):
    for j in range(length -i -1):
        print(' ', end="")
    for j in range(0, i+1):
        print(word[j], end="")
    for k in range (i-1, -1, -1):
        print (word[k], end="")
    print()
for l in range (0,length):
    for j in range(l) :
        print(' ', end="")
    for m in range (0,length-l-1):
        print(word[m], end ="")
    for n in range (length-l-1,-1,-1):
        print(word[n], end="")
    print()