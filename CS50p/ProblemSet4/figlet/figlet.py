import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()


if len(sys.argv) == 3:
    if not(sys.argv[1] == '-f' or sys.argv[1] == '-font'):
        sys.exit("Invalid usage")
    elif sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    else:
        s = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(s))
elif len(sys.argv) == 1:
    s = input("Input: ")
    rfont = random.choice(fonts)
    figlet.setFont(font=rfont)
    print(figlet.renderText(s))
else:
    sys.exit("Invalid usage")


