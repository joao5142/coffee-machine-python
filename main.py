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
should_continue=True
cost=0
can_buy=False
def print_report():
    global cost
    water=resources["water"]
    milk=resources["milk"]
    coffe=resources["coffee"]
    format_money = "{:.2f}".format(cost)
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffe}g")
    print(f"Money:${format_money}")

def verify_resources(coffee,coins_value):
    """Verify and return if resources are sufficient"""
    drink=MENU[coffee]
    drink_cost=drink["cost"]
    drink_water=drink["ingredients"]["water"]

    if (coffee != "espresso"):
        drink_milk = drink["ingredients"]["milk"]
    else :
        drink_milk=0
    drink_coffee=drink["ingredients"]["coffee"]

    can_buy=False
    if(coins_value>=drink_cost):
        if(resources["water"]<drink_water):
             print( "Sorry there if not enough water.")
        elif(resources["milk"]<drink_milk):
            print("Sorry there if not enough milk.")
        elif (resources["coffee"]<drink_coffee):
            print("Sorry there if not enough coffee.")
        else:
            print(f"Here is your {answer}☕.Enjoy!")
            can_buy=True
    else:
        print("Sorry there is not enough money.")

    return can_buy

def process_coins():
    quarters_value=int(input("how many quarters?: "))
    dimes_value=int(input("how many dimes?: "))
    nickles_value=int(input("how many nickles?: "))
    pennies_value=int(input("how many pennies?: "))

    amount=0.25 *quarters_value+0.1*dimes_value+0.05*nickles_value+0.01*pennies_value;

    return amount

def process_payment(item,coins_value):
    drink_value=float(MENU[item]["cost"])

    if(coins_value>drink_value):
        money_refused=float(coins_value)-drink_value
        format_money = "{:.2f}".format(money_refused)

        print(f"Here is ${format_money} dollars in change.")
        return drink_value
    else:
        return drink_value

def build_coffe(coffee):
    drink = MENU[coffee]
    drink_cost = drink["cost"]
    drink_water = drink["ingredients"]["water"]
    drink_coffee = drink["ingredients"]["coffee"]

    if (coffee != "espresso"):
        drink_milk = drink["ingredients"]["milk"]
        resources["milk"] = resources["milk"] - drink_milk

    resources["water"]=resources["water"]-drink_water
    resources["coffee"] = resources["coffee"] - drink_coffee

# TODO 1. Ask to the user input
# TODO 2. Verify if the resources are sufficient
# TODO 3. Insert coins
# TODO 4. Verify if coins is enoghout to buy

while should_continue:
    answer=input("What Would you like ? (espresso/latte/cappuccino): ").lower()
    print("Please insert coins.")

    if(answer=="off"):
        should_continue=False
        break
    elif(answer=="report"):
        print_report()
    elif(answer== "latte")or (answer=="espresso")or(answer=="cappuccino"):
       coins_value=process_coins()
       can_buy= verify_resources(answer,coins_value)

    if(can_buy):
       cost+= process_payment(answer,coins_value)
       build_coffe(answer)
       can_buy = False
