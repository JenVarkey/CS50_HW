import random

while True:
    try:
        maxNum = int(input("Level: "))
        if maxNum < 1:
            continue
        break
    except ValueError:
        continue

num = random.randint(1, maxNum)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        if guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue


