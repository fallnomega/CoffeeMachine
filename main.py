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
    # print(("What would you like?\n1 - Espresso\n2 - Latte\n3 - Cappuccino)"
    #                   "\nUse 1, 2, or 3 for the selection: "))
    # selection = 0

    # Turn off the Coffee Machine by entering “off” to the prompt.
    if selection == 'off':
        turn_off()
    # Print report.
    elif selection == 'report':
        print_report()
    elif selection != '1' and selection != '2' and selection != '3':
        print("\n\nWrong selection, try again\n\n")
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
          f"Money: ${resources['money']}\n\n")
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
        print ("Checking latte resources.")
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


# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

def process_coins(drink_selection):
    drink_name =list(MENU)[int(drink_selection)-1]
    print ("PROCESSING COINS CALLED")
    print(f"Please insert coins to pay for your {drink_name}")
    inserted_quarters = 0
    inserted_dimes = 0
    inserted_nickles = 0
    inserted_pennies = 0

    quarters = .25
    dimes = .10
    nickles = .05
    pennies = .01

    return


# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

def check_transaction_successful():
    return


# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.

def make_coffee(drink_to_be_made):

    return


turn_off_machine = False
while turn_off_machine != True:
    drink_choice = order_drink()
    make_coffee(drink_choice)
    # Check resources sufficient?
    resource_check = check_resources_availability(drink_choice)
    if resource_check == 0:
        continue
    process_coins(drink_choice)
    turn_off()
