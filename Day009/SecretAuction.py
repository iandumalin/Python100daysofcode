logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
        Welcome to the auction.
'''
print(logo)
bidder_list = []
finished = False
while not finished :
    bidder = {}
    bidder["name"] = input("What is your name?: ")
    bidder["bid"] = int(input("how much do you bid?: €"))
    bidder_list.append(bidder)
    if input("are there other bidders? ('yes' or 'no'): ") == "no" :
        finished = True

highest_bidder = {}
max_value = 0 
for bidder in bidder_list :
    if max_value < bidder["bid"] :
        max_value = bidder["bid"]
        highest_bidder = bidder
print(f"The winner is {highest_bidder['name']} with a bid of €{highest_bidder['bid']}")