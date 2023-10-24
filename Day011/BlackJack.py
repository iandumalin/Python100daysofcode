# This is the code for the game of Blackjack
# Here are the rules of the game:
# - The goal of the game is to have a hand value of 21 or as close to 21 as possible without going over
# - Each player is dealt two cards, and can choose to "hit" (receive another card) or "stand" (keep their current hand)
# - Face cards (Jack, Queen, King) are worth 10 points, Aces are worth 1 or 11 points (whichever is more advantageous to the player)
# - If a player's hand exceeds 21 points, they "bust" and lose the game
# - If both the player and dealer have the same hand value, it is a "push" and the player's bet is returned
# - If the player's hand is closer to 21 than the dealer's hand, the player wins and receives a payout of 1:1 (their bet plus an equal amount)
# - If the dealer's hand is closer to 21 than the player's hand, the player loses their bet
# - The dealer stops at 17 or higher.
import random
finished = False
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'       Made in Python      |__/           
"""
value_dictionary = {
    "A" : 11,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10
}
cards = list(value_dictionary.keys())

def calculate_score(card_list) :
    score = 0
    for card in card_list :
        score += value_dictionary[card]
        if card == "A" and score > 21 :
            score -= 10
    return score

def start(player_cards, cpu_cards) :
    global finished
    for i in range(2) :
        player_cards.append(random.choice(cards))
        cpu_cards.append(random.choice(cards))
    print(logo)
    
def end(player_cards, cpu_cards) :
    global finished
    player_score = calculate_score(player_cards)
    cpu_score = calculate_score(cpu_cards)
    while cpu_score < 17 :
        cpu_cards.append(random.choice(cards))
        cpu_score = calculate_score(cpu_cards)
        
    print(
f"""#### FINISH ####
Your cards: {player_cards}
Your score: {player_score}

Dealer cards: {cpu_cards}
Dealer score: {cpu_score}""")
    
    if player_score > 21 or (cpu_score > player_score and cpu_score <= 21) :
        print ("You lose!")
    elif player_score == cpu_score :
        print ("It's a push!")
    else :
        print ("You win!")
    print("Thanks for playing!")
    finished = True
    
def update(player_cards, cpu_cards) :
    global finished
    player_score = calculate_score(player_cards)
    cpu_score = calculate_score(cpu_cards)
    print(f"Your cards: {player_cards}\nYour score: {player_score}\n\nDealer cards: [{cpu_cards[0]}, '?']\n")
    if player_score > 21 or cpu_score == 21 :
        finished = True
        end(player_cards, cpu_cards)
        return
    else :
        action = input("Do you want to [S]tand or [H]it?").lower()
        if action == "stand" or action == "s" :
            finished = True
            end(player_cards, cpu_cards)
            return
        elif action == "hit" or action == "h" :
            player_cards.append(random.choice(cards))
        else :
            print("Invalid input. Please try again.")
    
player_cards = []
cpu_cards = []
start(player_cards, cpu_cards)
while not finished : update(player_cards, cpu_cards)