amountDue = 50
print("Amount Due: 50")
ref = amountDue
num = 0
while num < 50:
    amountGiven = int(input("Insert Coin: "))
    if amountGiven == 25 or amountGiven == 10 or amountGiven == 5:
        num+=amountGiven
        amountDue -= amountGiven
    if amountDue > 0:
        print("Amount Due: " + str(amountDue))
print("Change Owed: " + str(amountDue * -1))
