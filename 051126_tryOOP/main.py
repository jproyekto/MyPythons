import json

#load data
with open("data.json", "r", encoding="utf8") as f:
    data = json.load(f)
# declare
menu_items = data["menu_items"]
currency = data["CURRENCY"]


def main():
    is_on = True

    while is_on:
        print("``````````````````````````````````````````````")
        print(f"Welcome to Candy Shop")
        for item_name, item_data in menu_items.items():
            print(f"{currency}{item_data["cost"]} {item_name}")
        print("``````````````````````````````````````````````")




if __name__ == "__main__":
    main()