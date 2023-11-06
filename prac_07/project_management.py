"""
CP1404 - Project Management Program
"""
import datetime
from project import Project

FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date"
        "\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def main():
    projects = load_projects(FILENAME)

    print(MENU)
    projects.sort()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = "Load to file: "  # error checking needed?
            projects = load_projects(filename)
        elif choice == "S":
            filename = "Save to file: "  # error checking needed?
            save_projects(filename, projects)
        elif choice == "D":
            print("Incomplete projects:")
            print("\t" + "\n\t".join(str(project) for project in projects if not project.is_complete()))
            print("Completed projects:")
            print("\t" + "\n\t".join(str(project) for project in projects if project.is_complete()))
        elif choice == "F":
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            start_date = format_date(date_string)
            print("\n".join(str(project) for project in projects if project.date > start_date))
        elif choice == "A":
            print("Lets add a new project")
            new_project = Project(*get_new_project_details())
            projects.append(new_project)
        elif choice == "U":
            for i, project in enumerate(projects):
                print(i, project)
            project_choice = int(input("Project choice: "))  # error checking needed
            print(projects[project_choice])
            update_project(projects, project_choice)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")
    save_projects(FILENAME, projects)


def update_project(projects, project_choice):
    new_percentage = input("New percentage: ")
    new_priority = input("New priority: ")
    if new_percentage != "":  # can extract function + can change if statement "" = false
        try:
            projects[project_choice].completion = int(new_percentage)
        except ValueError:
            print("Percentage must be a number")
    if new_priority != "":
        try:
            projects[project_choice].priority = int(new_priority)
        except ValueError:
            print("Priority must be  number")


def get_new_project_details():
    name = get_valid_string("Name: ")
    date_string = input("Start date (dd/mm/yyyy): ")  # error checking needed
    start_date = format_date(date_string)
    priority = get_valid_number(int, "Priority: ")
    cost = get_valid_number(float, "Cost estimate: $")
    completion = get_valid_number(int, "Percent complete: ")
    return name, start_date, priority, cost, completion


def get_valid_string(prompt):
    string = input(prompt)
    while string == "":
        print("Invalid string cannot be empty.")
        string = input(prompt)
    return string


def get_valid_number(number_type, prompt):
    is_valid = False
    while not is_valid:
        try:
            number = number_type(input(prompt))
            if number < 0:
                print("Invalid number should be >= 0.")
            else:
                is_valid = True
        except ValueError:
            print("Invalid number")
    return number


def format_date(date_string):
    formatted_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    return formatted_date


def load_projects(filename):
    projects = []
    with open(filename) as infile:
        infile.readline()
        for line in infile:
            parts = line.strip().split("\t")
            start_date = format_date(parts[1])
            project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as outfile:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=outfile)
        for project in projects:
            print(f"{project.name}\t{project.date}\t{project.priority}\t"
                  f"{project.cost}\t{project.completion}\t", file=outfile)


main()
