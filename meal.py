def main():
    time = convert(input("What time is it? "))
    if time >= 7 and time <=8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")
def convert(time):
    numOne = float(time[0:time.find(":")])
    numTwo = float(time[time.find(":") + 1:])
    numTwo /=60

    return numOne + numTwo


if __name__ == "__main__":
    main()
