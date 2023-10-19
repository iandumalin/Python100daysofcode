logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|                  Python Calculator
"""

print(logo)
def mathaction(type, number_one, number_two) :
    try:
        if type == '+' :
            return number_one + number_two
        elif type == '-' :
            return number_one - number_two
        elif type == '*' :
            return number_one * number_two
        elif type == '/' :
            return number_one / number_two
        else :
            return "Error"
    except:
        return "Error"

operator = ['+', '-', '*', '/']

finished = False 
while not finished :
    number_one = float(input("What's the first number? "))
    number_two = float(input("What's the second number? "))
    type = input(f"What's the operation? ({operator})")
    result = mathaction(type, number_one, number_two)
    print(f"{number_one} {type} {number_two} = {result}")
    if input("Do you want to continue? Type 'y' or 'n': ") == 'n' :
        finished = True
        print("Goodbye")