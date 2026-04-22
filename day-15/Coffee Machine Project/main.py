



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}
money = 0




def choice_menu(choice):
    global money
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif choice == "off":
        return 0
    elif choice == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
            if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                print("Please insert coins: ")
                quarters = int(input("How many quarters: "))
                dimes = int(input("How many dimes: "))
                nickels = int(input("How many nickels: "))
                pennies = int(input("How many pennies: "))
                total_value = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
                if total_value >= MENU["espresso"]["cost"]:
                    change = total_value - MENU["espresso"]["cost"]
                    money += MENU[choice]["cost"]
                    print(f"Here is your change ${change:.2f} ")
                    print("Here is your espresso ☕️. Enjoy!")
                    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                else:
                    print("Sorry that's not enough money. Money refunded.")

            else:
                print("There is not enough coffee.")
        else:
            print("There is not enough water.")
    elif choice == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
            if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                    print("Please insert coins: ")
                    quarters = int(input("How many quarters: "))
                    dimes = int(input("How many dimes: "))
                    nickels = int(input("How many nickels: "))
                    pennies = int(input("How many pennies: "))
                    total_value = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
                    if total_value >= MENU["latte"]["cost"]:
                        change = total_value - MENU["latte"]["cost"]
                        money += MENU[choice]["cost"]
                        print(f"Here is your change ${change:.2f} ")
                        print("Here is your latte ☕️. Enjoy!")
                        resources["water"] -= MENU["latte"]["ingredients"]["water"]
                        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                else:
                    print("There is not enough coffee.")
            else:
                print("There is not enough milk.")
        else:
            print("There is not enough water.")
    elif choice == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
            if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
                    print("Please insert coins: ")
                    quarters = int(input("How many quarters: "))
                    dimes = int(input("How many dimes: "))
                    nickels = int(input("How many nickels: "))
                    pennies = int(input("How many pennies: "))
                    total_value = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
                    if total_value >= MENU["cappuccino"]["cost"]:
                        change = total_value - MENU["cappuccino"]["cost"]
                        money += MENU[choice]["cost"]
                        print(f"Here is your change ${change:.2f} ")
                        print("Here is your cappuccino ☕️. Enjoy!")
                        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                else:
                    print("There is not enough coffee.")
            else:
                print("There is not enough milk.")
        else:
            print("There is not enough water.")
    return None

while resources["water"] > 0 or resources["milk"] > 0 or resources["coffee"] > 0:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        break
    choice_menu(user_choice)






