"""
CP1404 - Guitars
estimate - 40 mins 11:20
actual - 40 mins, 12:00
"""
from prac_06.guitar import Guitar


def main():
    """"""
    guitars = []
    print("My guitars!")
    add_guitars(guitars)

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def add_guitars(guitars):
    """"""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        print(guitar, "added.\n")
        guitars.append(guitar)
        name = input("Name: ")


main()
