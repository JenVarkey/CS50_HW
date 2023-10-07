import sys
from pyfiglet import Figlet
import random

errorMessage = "Invalid usage"
if sys.argv.__len__() == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    figlet = Figlet()
    specifiedFont = sys.argv[2]
    availableFonts = figlet.getFonts()
    validInput = False
    for x in availableFonts:
        if x == specifiedFont:
            validInput = True
    if validInput == False:
        sys.exit(errorMessage)
    userInput = input("Input: ")
    figlet = Figlet(specifiedFont)
    print(figlet.renderText(userInput))
elif sys.argv.__len__() == 1:
    figlet = Figlet()
    availableFonts = figlet.getFonts()
    randNum = random.randint(0, availableFonts.__len__())
    userInput = input("Input: ")
    figlet = Figlet(availableFonts[randNum])
    print(figlet.renderText(userInput))
else:
    sys.exit(errorMessage)