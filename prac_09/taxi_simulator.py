"""
CP-1404 - Taxi Simulator
Estimate:
Actual:
"""

from taxi import Taxi
from silver_taxi_service import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            pass
        elif menu_choice == "d":
            pass
        else:
            print("Invalid option")
        print("Bill to date: $")
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>> ").lower()
    print("Total trip cost: $")
    print("Taxis are now:")
