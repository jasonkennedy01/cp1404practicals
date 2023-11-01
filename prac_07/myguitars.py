"""
CP1404 Practical
Estimate: 15 mins 10:53
actual:
"""
from guitar import Guitar


def main():
    """Display Guitars"""
    guitars = []
    with open("guitars.csv", "r") as infile:
        for line in infile:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    for guitar in guitars:
        print(guitar)
    guitars.sort()
    print("\nSorted Guitars")
    for guitar in guitars:
        print(guitar)


main()