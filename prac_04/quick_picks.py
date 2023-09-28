"""Program that generates a number of random quick picks determined by the user, with preset
boundaries and number of numbers per line."""
import random

RANDOM_NUMBER_LOW = 1
RANDOM_NUMBER_HIGH = 45
RANDOM_NUMBERS_PER_LINE = 6


def main():
    """Program that generates a number of quick picks based on user input."""
    number_of_lines = int(input("How many quick picks? "))
    for i in range(number_of_lines):
        quick_pick = generate_quick_pick()
        quick_pick.sort()
        print_quick_pick(quick_pick)


def print_quick_pick(quick_pick):
    """Print given quick pick with formatting."""
    for i in quick_pick:
        print(f"{i:2}", end=" ")
    print()


def generate_quick_pick():
    """Generate a random quick pick based on a preset number of numbers per line and
    boundaries, without duplicates."""
    quick_picks = []
    for i in range(RANDOM_NUMBERS_PER_LINE):
        number = random.randint(RANDOM_NUMBER_LOW, RANDOM_NUMBER_HIGH)
        while number in quick_picks:
            number = random.randint(RANDOM_NUMBER_LOW, RANDOM_NUMBER_HIGH)
        quick_picks.append(number)
    return quick_picks


main()
