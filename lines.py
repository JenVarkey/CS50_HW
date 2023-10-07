import sys

if sys.argv.__len__() < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv.__len__() > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].find(".py") == -1:
    sys.exit("Not a Python file")
try:
    count = 0
    with open(sys.argv[1].lstrip(), "r") as file:
        for line in file:
            if line.strip() != "" and line.strip().find("#")!= 0:
                count+=1
    print(count)
except FileNotFoundError:
    sys.exit("File does not exist")