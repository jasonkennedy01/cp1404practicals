# 1. Write to name.txt
name = input("Enter your name: ")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)

#  2. read name.txt
with open("name.txt") as in_file:
    print(f"Your name is {in_file.read()}")

# 3. add first and second numbers in numbers.txt
with open("numbers.txt") as in_file:
    total = 0
    for i in range(2):
        total += int(in_file.readline().strip())
    print(total)

# 4. add total for all lines in numbers.txt
with open("numbers.txt") as in_file:
    total = 0
    for line in in_file:
        total += int(line.strip())
    print(total)
