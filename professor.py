import random
def main():
    level = get_level()
    score = 0
    for x in range(10):
        numOne = generate_integer(level)
        numTwo = generate_integer(level)
        sum = numOne + numTwo
        failedAttempts = 0
        while True:
            try:
                answer = int(input(str(numOne) + " + " + str(numTwo) + " = "))
                if answer == sum:
                    score+=1
                    break
                else:
                    if failedAttempts < 2:
                        failedAttempts+=1
                        print("EEE")
                    else:
                        print(str(numOne) + " + " + str(numTwo) + " = " + str(sum))
                        break
            except ValueError:
                continue
    print(score)
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 3:
                return level
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()