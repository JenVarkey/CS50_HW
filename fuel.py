def main():
    print(gauge(convert(input("Fraction: "))))

def convert(fraction):
    num = float(fraction[0:fraction.find("/")])
    den = float(fraction[fraction.find("/")+1:])
    print()
    if den < num:
        raise ValueError
    if(num/den > 0.01):
        if(num/den < 0.99):
            percent = num/den
            percent = round(percent, 2) * 100
            percent = int(percent)
            return percent
        else:
            return 100
    else:
        return 0

def gauge(percentage):
    if percentage == 0:
        return "E"
    elif percentage == 100:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()