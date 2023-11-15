from silver_taxi_service import SilverServiceTaxi


hummer = SilverServiceTaxi("Hummer", 200, 2)
print(hummer)
hummer.drive(18)
print(hummer.get_fare())
print(hummer)
