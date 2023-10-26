from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()


def update():
    user_input = input(f"What would you like? {menu.get_items()}\n").lower()
    if user_input == "stop" :
        return False
    
    elif user_input == "report":
        coffee_machine.report()
        money_machine.report()
        
    elif user_input in menu.get_items() :
        item = menu.find_drink(user_input)
        print(f"{item.name} costs {item.cost}, please enter coins...")
        if coffee_machine.is_resource_sufficient(item) :
            if money_machine.make_payment(item.cost) :
                coffee_machine.make_coffee(item)
                
    else :
        print("Invalid input...")
    return True



while update(): ""