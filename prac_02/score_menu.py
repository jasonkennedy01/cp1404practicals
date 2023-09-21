"""
Program that gets a score, prints a result or displays stars, displayed as a menu.
"""
from score import determine_result


def main():
    """Menu program that gets a score, prints a result or displays stars."""
    score = get_valid_score()
    print_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"\n{result}\n")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid Choice")
        print_menu()
        choice = input(">>> ").upper()
    print("Goodbye")


def get_valid_score():
    """Get a valid score."""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score.")
        score = int(input("Score: "))
    return score


def print_menu():
    """Print the menu options."""
    print("""(G)et Score
(P)rint result
(S)how stars
(Q)uit""")


def print_stars(score):
    """Print as many stars as the score that is entered."""
    print("*" * score)


main()
