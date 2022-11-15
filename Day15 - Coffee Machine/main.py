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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${profit}")


def check_resource(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            print(f"Sorry there is not enough {items}")
            return False
    return True


def process_coin():
    print("Please insert coins. ")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.1
    total += int(input("how many nickles? ")) * 0.05
    total += int(input("how many pennis? ")) * 0.01
    return total


def check_transaction(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change")
        return True


def make_coffee(order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {choice} ☕️. Enjoy!")


def add_ingredients(water, milk, coffee):
    resources['water'] += water
    resources['milk'] += milk
    resources['coffee'] += coffee


def withdraw_profit():
    money = int(input("How much money do you want to withdraw? "))
    global profit
    if money > profit:
        print("The amount of money you withdraw is larger than the profit. Please try agian!")
        return withdraw_profit()
    else:
        profit -= money


is_on = True

while is_on:
    choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        report()
    elif choice == 'add':
        amount_of_water = int(input('The amount of water input to the coffee machine: '))
        amount_of_milk = int(input('The amount of milk input to the coffee machine: '))
        amount_of_coffee = int(input('The amount of coffee input to the coffee machine: '))
        add_ingredients(amount_of_water, amount_of_milk, amount_of_coffee)
    elif choice == 'withdraw':
        withdraw_profit()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if check_resource(drink['ingredients']):
            payment = process_coin()
            if check_transaction(payment, drink['cost']):
                make_coffee(drink['ingredients'])
    else:
        print("Invalid input")
