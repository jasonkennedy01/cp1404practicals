min_password_length = int(input("Min passwprd length: "))
password = input("Password: ")
while len(password) < min_password_length:
    print("Invalid password length")
    password = input("Password: ")
print("*" * len(password))
