import random

user_choice = input("What do you choose? Rock, paper or scizzors?\n").lower()
rock_paper_scizzors = ["rock", "paper", "scizzors"]

user_number = rock_paper_scizzors.index(user_choice)
cpu_number = random.randint(0, 2)

print(f"You chose {rock_paper_scizzors[user_number]}!")
print(f"CPU chose {rock_paper_scizzors[cpu_number]}!")
number_pair = [user_number, cpu_number]

if number_pair[0] == number_pair[1] :
    print("\nDraw!")
elif number_pair == [0, 2] or number_pair == [1, 0] or number_pair == [2, 1] :
    print("\nYou win!")
elif number_pair == [2, 0] or number_pair == [0, 1] or number_pair == [1, 2] :
    print("\nYou lose!")