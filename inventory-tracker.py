# Simple Inventory Tracker - by Aliyu Abdulkadir Baba

inventory = {
    "Rice (50kg)": 20,
    "Indomie Carton": 35,
    "Peak Milk": 50
}

print("=== Current Inventory ===")
for item, qty in inventory.items():
    print(f"{item}: {qty} in stock")

# Add new stock
item = input("\nEnter item to add stock: ")
qty = int(input("How many to add? "))

if item in inventory:
    inventory[item] += qty
else:
    inventory[item] = qty

print("\n=== Updated Inventory ===")
for item, qty in inventory.items():
    print(f"{item}: {qty} in stock")

print("\nStock updated successfully!")
