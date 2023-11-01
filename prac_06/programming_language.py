"""Programming Languages Class."""


class ProgrammingLanguage:
    """Class that defines a programming language object."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise the programming language object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Display the programming language object in a str format."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if the programming language uses dynamic typing."""
        return self.typing == "Dynamic"
