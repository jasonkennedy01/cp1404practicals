"""
Program that converts a valid password to astericks.
"""


def main():
    """Program that converts a password of a set length to astericks."""
    min_password_length = int(input("Min password length: "))
    password = get_password(min_password_length)
    print_astericks(password)


def print_astericks(password):
    """Print a number of astericks"""
    print("*" * len(password))


def get_password(min_password_length):
    """Get a valid password."""
    password = input("Password: ")
    while len(password) < min_password_length:
        print("Invalid password length")
        password = input("Password: ")
    return password


main()
