def main():
    min_password_length = int(input("Min password length: "))
    password = get_password(min_password_length)
    print_astericks(password)


def print_astericks(password):
    print("*" * len(password))


def get_password(min_password_length):
    password = input("Password: ")
    while len(password) < min_password_length:
        print("Invalid password length")
        password = input("Password: ")
    return password


main()
