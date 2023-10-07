string = input("Expression: ")
x = float(string[0:string.find(" ")])
string = string[string.find(" "):]
y = string[1:2]
string = string[3:]
z = float(string)
if y == "+":
    print(x + z)
if y == "-":
    print(x - z)
if y == "*":
    print(x * z)
if y == "/":
    print(x / z)
