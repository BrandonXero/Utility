## Inputs we need
# total rent
# total food 
# electricity
# charge per unit
# Person living in the room

## output
#total amount you have to pay

rent = float(input("Enter the total rent:  "))
food = float(input("Enter the total food cost:  "))
electricity_units = float(input("Enter the electricity used (units): "))
charge_per_unit = float(input("Enter the charge per unit: "))
persons = int(input("Enter the number of people sharing: "))

# Calculate total electricity bill
total_electricity = electricity_units * charge_per_unit

# Calculate total cost
total_cost = rent + food + total_electricity

# Calculate per person share
amount_per_person = total_cost / persons

#Output
print("\n--- Bill Breakdown ---")
print(f"Rent: ${rent:.2f}")
print(f"Food: ${food:.2f}")
print(f"Electricity: ${total_electricity:.2f}")
print(f"Total cost: ${total_cost:.2f}")
print(f"Each person pays: ${amount_per_person:.2f}")

