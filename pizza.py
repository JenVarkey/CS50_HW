from tabulate import tabulate
import sys

if sys.argv.__len__() < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv.__len__() > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].find(".csv") == -1:
    sys.exit("Not a CSV file")
try:
    pizzaList = []
    with open('regular.csv', newline='\n') as file:
        for row in file.readlines():
            pizzaList.append(row.strip().split(","))

    print(tabulate(pizzaList, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("Not a CSV file")