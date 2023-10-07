fraction = input("Fraction: ")
while True:
    try:

        num = float(fraction[0:fraction.find("/")])
        den = float(fraction[fraction.find("/")+1:])
        if num <= den and fraction.find(".") == -1:
            break
        else:
            fraction = input("Fraction: ")
    except ValueError:
        print("Made it here")
        fraction = input("Fraction: ")



try:
    if(num/den > 0.01):
        if(num/den < 0.99):
           percent = num/den
           percent = round(percent, 2) * 100
           percent = int(percent)
           print(str(percent) + "%")
        else:
            print("F")
    else:
        print("E")
except ZeroDivisionError:
    print("E")