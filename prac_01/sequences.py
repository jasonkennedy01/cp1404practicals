x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
if x % 2 == 0:
    even_offset = 0
    odd_offset = 1
else:
    even_offset = 1
    odd_offset = 0
print("(E)ven\n(O)dd\n(S)quares\n(Q)uit")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "E":
        for i in range(x + even_offset, y + 1, 2):
            print(i, end=" ")
        print()
    elif choice == "O":
        for i in range(x + odd_offset, y + 1, 2):
            print(i, end=" ")
        print()
    elif choice == "S":
        for i in range(x, y + 1):
            print(i ** 2, end=" ")
        print()
    else:
        print("Invalid choice")
    print("(E)ven\n(O)dd\n(S)quares\n(Q)uit")
    choice = input(">>> ").upper()
print("Thank you")
