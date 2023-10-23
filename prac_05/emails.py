"""
Emails
Estimate: 20mins 10:26
Actual:   24mins 10:50
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        email_to_name[email] = name
        email = input("Email: ")

    for item in email_to_name.items():
        print(f"{item[-1]} ({item[0]})")


def get_name(email):
    parts = email.split("@")
    names = parts[0].split(".")
    name = " ".join(name for name in names).title()
    is_name = input(f"Is your name {name}? (Y/n) ").upper()
    if is_name == "" or is_name == "Y":
        return name
    name = input("Name: ").title()
    return name


main()
