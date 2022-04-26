COLOR_TO_CODE = {"absolute zero": "#0048ba", "Acid Green": "#b0bf1a", "aliceBlue": "#f0f8ff",
                 "alizarin crimson": "#e32636",
                 "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc"}
color = input("enter the colour name: ").lower()
if color in COLOR_TO_CODE:
    print("The code for \"{}\" is {}".format(color, COLOR_TO_CODE.get(color)))
else:
    print("invalid input try again!")


