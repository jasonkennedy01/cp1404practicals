"""Test the guitar class"""
from prac_06.guitar import Guitar


def test_guitars():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another guitar", 2016, 300.99)
    guitar3 = Guitar("50 year old guitar", 1973, 1000.99)
    print(guitar1, guitar2, sep="\n")

    print(f"{guitar1.name} get_age() - Expected 101. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 7. Got {guitar2.get_age()}")
    print(f"{guitar3.name} get_age() - Expected 50. Got {guitar3.get_age()}")
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")
    print(f"{guitar3.name} is_vintage() - Expected True. Got {guitar3.is_vintage()}")


test_guitars()
