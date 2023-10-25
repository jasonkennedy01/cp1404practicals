"""Test the guitar class"""
from prac_06.guitar import Guitar


def test_guitars():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another guitar", 2016, 300.99)
    print(guitar1, guitar2, sep="\n")


test_guitars()
