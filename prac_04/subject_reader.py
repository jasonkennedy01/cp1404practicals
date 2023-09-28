"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_subject_details(data)


def print_subject_details(subjects):
    """Print subject details including subject code, lecturer and number of students"""
    for subject in subjects:
        subject_code = subject[0]
        lecturer = subject[1]
        number_of_students = subject[-1]
        print(f"{subject_code} is taught by {lecturer:12} and has {number_of_students:3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        data.append(parts)
    input_file.close()
    return data


main()
