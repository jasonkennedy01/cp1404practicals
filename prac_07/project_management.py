"""
CP1404 - Project Management Program
"""

from project import Project

FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date"
        "\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def main():
    projects = load_projects(FILENAME)

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = "Load to file: "
            projects = load_projects(filename)
        elif choice == "S":
            filename = "Save to file: "
            save_projects(filename, projects)
        elif choice == "D":
            print("Incomplete projects:")
            for project in projects:
                if not project.is_complete():
                    print(project)
            # print(project for project in projects if not project.is_complete())
            print("Completed projects:")
            for project in projects:
                if project.is_complete():
                    print(project)
            # print(project for project in projects if project.is_complete())
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")
    save_projects(FILENAME, projects)


def load_projects(filename):
    projects = []
    with open(filename) as infile:
        infile.readline()
        for line in infile:
            parts = line.strip().split("\t")
            project = Project(*parts)  # this will need to change when adding date formatting i think
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as outfile:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=outfile)
        for project in projects:
            print(f"{project.name}\t{project.date}\t{project.priority}\t"
                  f"{project.cost}\t{project.completion}\t", file=outfile)


main()
