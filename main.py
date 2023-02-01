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
    "water": 500,
    "milk": 200,
    "coffee": 100,
    "money": 100
}
QUARTERS = .25
DIMES = .10
NICKLES = .05
PENNIES = .01


# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def order_drink():
    selection = input("What would you like?\n1 - Espresso\n2 - Latte\n3 - Cappuccino)"
                      "\nUse 1, 2, or 3 for the selection: ")
    # Turn off the Coffee Machine by entering “off” to the prompt.
    if selection == 'off':
        turn_off()
    # Print report.
    elif selection == 'report':
        print_report()
    elif int(selection) > 3:
        print("\n\nWrong selection, try again\n\n")
        exit()
    else:

        return selection


def turn_off():
    print("\n\nTurning off the machine. Good bye!\n\n")
    exit()
    return


def print_report():
    print(f"\n\nReport on resource levels:\n"
          f"Water: {resources['water']}m\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}\n"
          f"Profit: ${resources['money'] - 100}\n\n")
    return


def check_resources_availability(drink_to_check):
    # espresso check
    if drink_to_check == '1':
        print("Checking espresso resources.")
        if int(resources['water']) < int(MENU['espresso']['ingredients']['water']):
            print("Sorry there is not enough water.")
            return 0
        elif int(resources['coffee']) < int(MENU['espresso']['ingredients']['coffee']):
            print("Sorry there is not enough coffee beans.")
            return 0
        else:
            return 1

    # latte check
    if drink_to_check == '2':
        print("Checking latte resources.")
        if int(resources['water']) < int(MENU['latte']['ingredients']['water']):
            print("Sorry there is not enough water.")
            return 0
        elif int(resources['milk']) < int(MENU['latte']['ingredients']['milk']):
            print("Sorry there is not enough milk.")
            return 0
        elif int(resources['coffee']) < int(MENU['latte']['ingredients']['coffee']):
            print("Sorry there is not enough coffee beans.")
            return 0
        else:
            return 1

    # Cappuccino check
    if drink_to_check == '3':
        print("Checking cappuccino resources.")
        if int(resources['water']) < int(MENU['cappuccino']['ingredients']['water']):
            print("Sorry there is not enough water.")
            return 0
        elif int(resources['milk']) < int(MENU['cappuccino']['ingredients']['milk']):
            print("Sorry there is not enough milk.")
            return 0
        elif int(resources['coffee']) < int(MENU['cappuccino']['ingredients']['coffee']):
            print("Sorry there is not enough coffee beans.")
            return 0
        else:
            return 1
    return


# Process coins.
def process_coins(drink_selection):
    drink_name = list(MENU)[int(drink_selection) - 1]
    print(f"Please insert coins to pay for your {drink_name}.\n"
          f"The total cost is: ${MENU[drink_name]['cost']} ")

    inserted_quarters = int(input("How many quarters to insert?") or 0)
    inserted_dimes = int(input("How many dimes to insert?") or 0)
    inserted_nickles = int(input("How many nickles to insert?") or 0)
    inserted_pennies = int(input("How many pennies to insert?") or 0)
    total_inserted = round((inserted_quarters * QUARTERS) + (inserted_dimes * DIMES) + (inserted_nickles * NICKLES) + (
            inserted_pennies * PENNIES), 2)
    print(f"Total inserted is: ${round(total_inserted, 2)}")
    # Check transaction successful?
    if check_transaction_successful(total_inserted, drink_name) is False:
        print("Sorry that's not enough money. Money refunded.")
        exit()
    else:
        if float(MENU[drink_name]['cost']) < total_inserted:
            print(f"{total_inserted} - {float(MENU[drink_name]['cost'])}")
            change = total_inserted - float(MENU[drink_name]['cost'])
            resources['money'] += MENU[drink_name]['cost']
            print(f"Here is ${change} dollars in change")

        else:
            resources['money'] += MENU[drink_name]['cost']
    return


def check_transaction_successful(inserted_money, drink_name):
    if int(MENU[drink_name]['cost']) > inserted_money:
        return False
    else:
        return True


# Make Coffee.
def make_coffee(drink_to_be_made):
    if int(drink_to_be_made) == 1:
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        return
    if int(drink_to_be_made) == 2:
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        return
    else:
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        return
    return


turn_off_machine = False
while turn_off_machine != True:
    drink_choice = order_drink()
    print_report()
    # Check resources sufficient?
    resource_check = check_resources_availability(drink_choice)
    if resource_check == 0:
        continue
    process_coins(drink_choice)
    make_coffee(drink_choice)
    print_report()
    print(f"Here is your {list(MENU)[int(drink_choice) - 1]}. Enjoy!")
    turn_off()
