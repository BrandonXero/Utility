# EasyRenter - Beginner-Friendly Apartment Bill Calculator

def get_float_input(prompt):
    # "Helper function to get a positive float from user"
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")    

def get_int_input(prompt):
     # "Helper function to get a positive integer from user"
    while True:
      try:
            value = int(input(prompt))
            if value < 1:
                print("Please enter a number greater thab 0.")
            else:
                return value
      except ValueError:
        print("Invalid input. Please enter and integer.")

# Step 1: Get the basic information
print("Welcome to my Easy Renter - Apartment Bill calculator!\n")

num_people = get_int_input("How many people are sharing this apartment? ")
people = []
for i in range(num_people):
     name = input(f"Enter the name of person #{i+1}: ").strip()
     people.append(name)

# Step 2: Get main costs
rent = get_float_input("Enter the total rent for the apartment: ")
food = get_float_input("Enter the total cost of food: ")

# Step 3: Add utilities
utilites = {}
num_utilities = get_int_input("How many additional utilities (electricity, water, internet, etc.) do you have?: ")

for i in range(num_utilities):
     utility_name = input(f"Enter the name of utility #{i+1}: ").strip()
     cost = get_float_input(f"Enter the total cost for {utility_name}: ")
     utilites[utility_name] = cost

# Step 4: Calculate totals
total_utilities = sum(utilites.values())
total_cost = rent + food + total_utilities
amount_per_person = total_cost / num_people

# Step 5: Print breakdown
print("\n--- Monthly Bill Breakdown ---")
print(f"Rent: ${rent:.2f}")
print(f"Food: ${food:.2f}")
for name, cost in utilites.items():
     print(f"{name}: ${cost:.2f}")
print(f"Total cost: ${total_cost:.2f}\n")

print("--- Each Person Pays ---")
for person in people:
     print(f"{person}: ${amount_per_person:.2f}")
