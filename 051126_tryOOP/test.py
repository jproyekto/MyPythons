import json

#load data
with open("data.json", "r", encoding="utf8") as f:
    data = json.load(f)


menu_items = data["menu_items"]
currency = data["CURRENCY"]


print("``````````````````````````````````````````````")
print(f"Welcome to Candy Shop")
for item_name, item_data in menu_items.items():
    print(f"{currency}{item_data["cost"]} {item_name}")
print("``````````````````````````````````````````````")

user_order = input("Enter your order:").lower()

# find order
for item_name, item_data in menu_items.items():
    # print(f"Name: {item_name} | Data: {item_data}")
    if item_name.lower() == user_order:
        print(f"Name: {item_name} | Data: {item_data}")


