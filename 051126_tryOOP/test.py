import json

#load data
with open("data.json", "r") as f:
    data = json.load(f)

# menu_items = ", ".join(data["menu_items"].keys())

print(f"Welcome to Candy Shop")

for m in data["menu_items"]:
    print(m)

user_choice = input("Enter your order:").lower()
print(user_choice)

print(data["menu_items"][user_choice]["cost"])

