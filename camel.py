case = input("camelCase: ")
newWord = ""
i = 0
while i < case.__len__():
    if case[i:i+1].istitle():
        newWord+= "_" + case[i:i+1].lower()
    else:
        newWord+= case[i:i+1]
    i+=1

print("snake_case: " + newWord)
