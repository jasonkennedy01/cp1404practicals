"""
CP1404 Practical
Estimate: 15 mins 10:53
actual:
"""
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Displays guitars, get new guitars from user and saves to a file."""
    guitars = []
    load_guitars(FILENAME, guitars)
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted Guitars")
    display_guitars(guitars)

    add_guitars(guitars)
    guitars.sort()
    display_guitars(guitars)
    save_guitars(FILENAME, guitars)


def display_guitars(guitars):
    """Display the guitars in a list."""
    for guitar in guitars:
        print(guitar)


def load_guitars(filename, guitars):
    """Load guitars from a file and store into a list."""
    with open(filename, "r") as infile:
        for line in infile:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)


def save_guitars(filename, guitars):
    """Save a list of guitars to a file."""
    with open(filename, "w") as outfile:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=outfile)


def add_guitars(guitars):
    """Add guitars to a list of guitars until the user stops."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        print(guitar, "added.\n")
        guitars.append(guitar)
        name = input("Name: ")


main()
