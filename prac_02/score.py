"""
CP1404/CP5632 - Practical
Program to determine a result from a score.
"""
import random


def main():
    """Program to determine a result from an entered and random score."""
    score = float(input("Enter score: "))
    user_result = determine_result(score)
    print(user_result)
    random_result = determine_result(random.randint(0, 100))
    print(random_result)


def determine_result(score):
    """Determine result based on score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
