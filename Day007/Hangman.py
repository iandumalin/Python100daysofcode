import random

word_list = ["aardvark", "baboon", "camel", "dimetrodon"]
word = random.choice(word_list)
display_word = []
word_length = len(word)
for _ in range(word_length) :
    display_word.append("")
print(f"DEBUG: {word}")
finished = False
life_counter = 3

while not finished :
    print(display_word)
    guess_letter = input("Guess a letter: ").lower()
    if len(guess_letter) > 1 :
        print("Please only guess one letter at a time.")
    if not guess_letter in word :
        life_counter -= 1
        print(f"Wrong letter! Please try again. Lives: {life_counter}")
        if life_counter <= 0 :
            print(f"No lives remaining, you lose! The word was {word}")
    else :
        for pos in range(word_length) :
            if word[pos] == guess_letter :
                display_word[pos] = guess_letter
    if not "?" in display_word :
        print("You win!")
        finished = True