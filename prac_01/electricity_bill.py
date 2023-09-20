# print("Electricity bill estimator")
# price_per_kwh = int(input("Enter cents per Kwh: "))
# daily_kwh_usage = float(input("Enter daily use in kWh: "))
# number_of_billing_days = int(input("Enter number of billing days: "))
# electricity_bill = number_of_billing_days * daily_kwh_usage * price_per_kwh / 100
# print(f"Estimated bill: ${electricity_bill:.2f}")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


print("Electricity bill estimator 2.0")
tariff_choice = int(input("Which tariff? 11 or 31: "))
daily_kwh_usage = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
if tariff_choice == 11:
    electricity_bill = number_of_billing_days * daily_kwh_usage * TARIFF_11
else:
    electricity_bill = number_of_billing_days * daily_kwh_usage * TARIFF_31
print(f"Estimated bill: ${electricity_bill:.2f}")
