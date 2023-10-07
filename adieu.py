import inflect
import sys
p = inflect.engine()
names = []
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print("Adieu, adieu, to " + p.join(names))
        sys.exit()
