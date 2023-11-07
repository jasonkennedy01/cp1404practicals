"""Guitar class"""


class Guitar:
    """Class for a guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise the guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Format the guitar object in a string format."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        """Returns the string representation of a guitar."""
        return str(self)

    def __lt__(self, other):
        """Compare guitars by age."""
        return self.year < other.year

    def get_age(self):
        """Calculate the age of the guitar from the current year."""
        age = 2023 - self.year
        return age

    def is_vintage(self):
        """Determines if a guitar is vintage based on its age."""
        return self.get_age() >= 50
