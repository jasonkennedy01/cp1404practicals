"""
CP-1404 - Taxi Simulator
"""

from taxi import Taxi
from silver_taxi_service import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    chosen_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            chosen_taxi = choose_taxi(taxis)
        elif menu_choice == "d":
            total_bill += drive_taxi(chosen_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    print("Taxis available:")
    display_taxis(taxis)
    return get_valid_choice(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_choice(taxis):
    try:
        taxi_choice = int(input("Choose taxi: "))
        return taxis[taxi_choice]
    except ValueError:
        print("Invalid taxi choice")
    except IndexError:
        print("Invalid taxi choice")


def drive_taxi(taxi):
    try:
        taxi.start_fare()
        distance = int(input("Drive how far? "))
        taxi.drive(distance)
        fare = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid distance")
    except AttributeError:
        print("You need a taxi to drive")
    return 0




if __name__ == '__main__':
    main()
