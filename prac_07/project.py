"""
CP1404 Project Class
Estimate: 5 hours
Time spent:
11:45 - 11:55 10mins
12:30 - 12:55 25mins
5:43 - 7:05 1hr, 22mins
3:00 -
"""
import datetime


class Project:
    """Project Class."""

    def __init__(self, name, date, priority, cost, completion):
        """Define the fields for the project object."""
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __repr__(self):
        """Returns a string representation for a project object."""
        return (f"{self.name}, start: {self.date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost}, completion: {self.completion}%")

    def is_complete(self):
        return self.completion == 100

    def __lt__(self, other):
        return self.priority < other.priority or self.date < other.date
