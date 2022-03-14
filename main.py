from art import logo
from data import MENU,resources

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

def verify_resources(coffee):
    """Verify and return if resources are sufficient"""
    drink=MENU[coffee]
    drink_cost=drink["cost"]
    drink_water=drink["ingredients"]["water"]

    if (coffee != "espresso"):
        drink_milk = drink["ingredients"]["milk"]
    else :
        drink_milk=0
    drink_coffee=drink["ingredients"]["coffee"]

    can_buy=True

    if(resources["water"]<drink_water):
        print( "Sorry there is not enough water.")
        return False
    elif(resources["milk"]<drink_milk):
        print("Sorry there is not enough milk.")
        return False
    elif (resources["coffee"]<drink_coffee):
        print("Sorry there is not enough coffee.")
        return False



    return can_buy

def process_coins():
    print("Please insert coins.")

    quarters_value=int(input("how many quarters?: "))
    dimes_value=int(input("how many dimes?: "))
    nickles_value=int(input("how many nickles?: "))
    pennies_value=int(input("how many pennies?: "))

    amount=0.25 *quarters_value+0.1*dimes_value+0.05*nickles_value+0.01*pennies_value;

    return amount

def process_payment(coffee,coins_value):
    drink_value=float(MENU[coffee]["cost"])

    if(coins_value>drink_value):
        money_refused=float(coins_value)-drink_value
        format_money = "{:.2f}".format(money_refused)

        print(f"Here is ${format_money} dollars in change.")
        return drink_value
    else:
        print(f"")
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

def transaction_successful(money,drink_cost):
    """Return true when the payment is accepted,or False if moneys is insufficient"""
    if(money>=drink_cost):
         return True
    else:
        print("Sorry that's not enough money.Money refunded.")

# TODO 1. Ask to the user input
# TODO 2. Verify if the resources are sufficient
# TODO 3. Insert coins
# TODO 4. Verify if coins is enough to buy
# TODO 5. Process the payment and add money to machine
print(logo)
while should_continue:
    choice=input("What Would you like ? (espresso/latte/cappuccino): ").lower()
    if(choice== "off"):
        should_continue=False
        break
    elif(choice == "report"):
        print_report()
    elif(choice == "latte")or (choice == "espresso")or(choice == "cappuccino"):
       resources_sufficient = verify_resources(choice)
       if(resources_sufficient):
            coins_value=process_coins()
            drink_cost=MENU[choice]["cost"]
            if(transaction_successful(coins_value,drink_cost)):
                can_buy=True


    if(can_buy):
       cost+= process_payment(choice, coins_value)
       build_coffe(choice)
       can_buy = False


