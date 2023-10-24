import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
tries = 0
answer = random.randint(1, 100)

if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy" :
    tries = 10
else :
    tries = 5
    
def try_guess() :
    global tries
    if tries <= 0 :
        print("You Lose.")
        return True
    global answer
    print(f"You have {tries} guesses left to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == answer : 
        print("Correct! Congrats!")
        return True
    elif guess > answer :
        print("Too high, guess again.")
        tries -= 1
        return False
    elif guess < answer :
        print("Too low, guess again.")
        tries -= 1
        return False
    else : return False
        
while not try_guess() : ""