"""
CP1404/CP5632 Practical
Colours and their hex code in a dictionary
"""

COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Ash Grey": "#b2beb5", "Beige": "#f5f5dc", "Black": "#000000",
                  "Brown": "#a52a2a", "Bubble Gum": "#ffc1cc", "Cardinal": "#c41e3a", "Celtic Blue": "#246bce",
                  "Chestnut": "#954535", "Corn": "#fbec5d"}

colour_name = input("Enter a colour: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter a colour: ").title()
