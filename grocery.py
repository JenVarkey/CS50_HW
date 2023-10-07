shoppingList = {}
try:
    while True:
        item = input().upper()
        inList = False
        for x in shoppingList:
            if x == item:
                num = shoppingList[item] + 1
                shoppingList[item] = num
                inList = True
        if not inList:
            shoppingList[item.upper()] = 1

except EOFError:
    for x in sorted(shoppingList):
        print(str(shoppingList[x]) + " " + x)
