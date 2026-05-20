import json
import process

from datetime import datetime


#load data
with open("data.json", "r", encoding="utf8") as f:
    data = json.load(f)
# declare
menu_items = data["menu_items"]
resources = data["resources"]
currency = data["CURRENCY"]
profit = data["profit"]


def main():
    is_on = True

    while is_on:
        print("``````````````````````````````````````````````")
        print(f"Welcome to Candy Shop")
        for item_name, item_data in menu_items.items():
            print(f"{currency}{item_data["cost"]} {item_name}")
        print("``````````````````````````````````````````````")
        u_order = process.getOrder()
        if u_order in ("x", "exit", "off", "quit"):
            is_on = False
            break
        elif u_order in ("p", "print", "r", "report"):
            print(f"\n|\tProfit {currency}{profit} as of {datetime.now()}\t|\n")
        else:
            processOrder = process.is_available(u_order,menu_items,resources)



if __name__ == "__main__":
    main()