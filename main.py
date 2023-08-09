MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


# TODO: 1.print report
def prt_resources():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')


# TODO: 2.check resources sufficient?
# get the choice and also allow some hidden input such as stop and report


def coffee_choice():
    customer_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_choice == "espresso":
        return 0
    elif customer_choice == "latte":
        return 1
    elif customer_choice == "cappuccino":
        return 2
    elif customer_choice == "report":
        return 3
    elif customer_choice == "off":
        return 4


def resources_check(coffee_type):
    if coffee_type["ingredients"]["water"] <= resources["water"]:
        if coffee_type["ingredients"]["milk"] <= resources["milk"]:
            if coffee_type["ingredients"]["coffee"] <= resources["coffee"]:
                return True
            else:
                print("Sorry there is not enough coffee")
                return False
        else:
            print("Sorry there is not enough milk")
            return False
    else:
        print("Sorry there is not enough water")
        return False


def coins_inserted():
    print("Please insert coins.")
    quarters_inserted = int(input("how many quarters?: "))
    dimes_inserted = int(input("how many dimes?: "))
    nickles_inserted = int(input("how many nickles?: "))
    pennies_inserted = int(input("how many pennies?: "))
    money = quarters_inserted * 0.25 + dimes_inserted * 0.10 + nickles_inserted * 0.05 + pennies_inserted * 0.01
    return money


is_on = True
while is_on:
    operations = coffee_choice()
    price = 0
    if operations == 0:
        coffee_type = MENU["espresso"]
        price = 1.5
        resources_sufficient = resources_check(coffee_type)
        if resources_sufficient:
            money_received = coins_inserted()
            if money_received >= price:
                changes = money_received - price
                print(f"Here is ${changes} in change.")
                print("Here is your espresso ☕. Enjoy!")
                resources["money"] += 1.5
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif operations == 1:
        coffee_type = MENU["latte"]
        price = 2.5
        resources_sufficient = resources_check(coffee_type)
        if resources_sufficient:
            money_received = coins_inserted()
            if money_received >= price:
                changes = money_received - price
                print(f"Here is ${changes} in change.")
                print("Here is your latte ☕. Enjoy!")
                resources["money"] += 2.5
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif operations == 2:
        coffee_type = MENU["cappuccino"]
        price = 3
        resources_sufficient = resources_check(coffee_type)
        if resources_sufficient:
            money_received = coins_inserted()
            if money_received >= price:
                changes = money_received - price
                print(f"Here is ${changes} in change.")
                print("Here is your cappuccino ☕. Enjoy!")
                resources["money"] += 3
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif operations == 3:
        prt_resources()
    elif operations == 4:
        is_on = False
    else:
        print("invalid input")


# TODO: 3.Process Coins.
# TODO: 4.Check transaction successful?
# TODO: 5.Make Coffee.
