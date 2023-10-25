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
    "coffee": 100
}

money = 0


def update() :
    user_input = input("What would you like? [E]spresso | [L]atte | [C]appuccino : ").lower()
    if user_input == "report" or user_input == "r" :
        generate_report()
    elif user_input == "espresso" or user_input == "e" :
        create_recipe("espresso")
    elif user_input == "latte" or user_input == "l" :
        create_recipe("latte")
    elif user_input == "cappuccino" or user_input == "c" :
        create_recipe("cappuccino")
    return True
      
def generate_report() :
    for resource in resources :
        print(f"{resource}: {resources[resource]}")
    print(f"money: €{money}")
      
def create_recipe(drink) :
    global resources, money
    item = MENU[drink]
    for resource in item["ingredients"] :
        if item["ingredients"][resource] > resources[resource] :
            print(f"Not enough {resource}, please select something else.")
            return
    print(f"{drink} costs €{item['cost']}. Please insert money...")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickels = int(input("How many nickels? : "))
    pennies = int(input("How many pennies? : "))
    coin_input = process_coins(quarters, dimes, nickels, pennies)
    if coin_input < item["cost"] :
        print(f"You didn't put in enough money. Refunding...")
        return
    else :
        for resource in item["ingredients"] :
            resources[resource] -= item["ingredients"][resource]
        print(f"Returning €{item['cost'] - coin_input}...\nEnjoy your {drink}!")   
        money += item['cost']
    
def process_coins(quarters, dimes, nickels, pennies) :
    amount = 0
    amount += (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return amount
    
    
while update() : ""