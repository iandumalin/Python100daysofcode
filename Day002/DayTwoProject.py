totalAmount = input("Welcome to the tip calculator\nWhat was the total bill?\n€")
percentageTip = input("What percentage tip would you like to give?\n")
totalPeople = input("How many people are there to split the bill?\n")

perPerson = round(float(totalAmount) * (1 + int(percentageTip) / 100) / int(totalPeople), 2)

print(f"Each person owes €{perPerson}")