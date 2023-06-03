import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

#list of fonts
get_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(get_fonts))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in get_fonts:
        figlet.setFont(font=sys.argv[2])
else:
      sys.exit("Invalid usage")



fig = input("Input: ")
print(figlet.renderText(fig))
