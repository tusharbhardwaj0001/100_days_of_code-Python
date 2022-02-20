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

MONEY = 0

def report():
    coffee= resources["coffee"]
    water = resources["water"]
    milk = resources["milk"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${round(MONEY,2)}")
    coffeeMachine()

    
def sufficientMaterial(choice):
    if resources["water"] < MENU[choice]["ingredients"]["water"]:
        print("  Sorry there is not enough water.")
        return False
    elif resources["milk"] < MENU[choice]["ingredients"]["milk"]:
        print("  Sorry ther is not enough milk.")
        return False
    elif resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
        print("  Sorry ther is not enough coffee.")
        return False
    else:
        return True


def insertCoins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    totalMoney = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return totalMoney

def sufficientMoney(money, choice):
    if money < MENU[choice]["cost"]:
        print("Sorry that's not enough. Money refunded.")
        return False
    elif money == MENU[choice]["cost"]:
        return True
    else:
        moneyChange = money - MENU[choice]["cost"]
        print(f"Here is ${round(moneyChange,2)} dollars in change.")
        return True

def makeCoffee(choice):
    global MENU
    global MONEY
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    MONEY += MENU[choice]["cost"]


def coffeeMachine():
    choice = input("  What would you like? (expresso/latte/cappuccino): ")
    if choice == "off":
        return
    elif choice == "report":
        report()
    else:
        if sufficientMaterial(choice):
            money = insertCoins()
            if sufficientMoney(money, choice):
                makeCoffee(choice)
                print(f"Here is your {choice}. Enjoy!")
                coffeeMachine()
            else:
                coffeeMachine()
        else:
            coffeeMachine()


coffeeMachine()

    
