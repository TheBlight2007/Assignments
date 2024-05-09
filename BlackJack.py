from colorama import Fore

suits = (Fore.BLACK + '\u2660' + Fore.RESET,  # Spades
         Fore.BLACK + '\u2663' + Fore.RESET,  # Clubs
         Fore.RED + '\u2665' + Fore.RESET,  # Hearts
         Fore.RED + '\u2666' + Fore.RESET)  # Diamonds
faces = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')
deck = []
for face in faces:
    for suit in suits:
        deck.append("[" + face + suit + "]")

print(Fore.GREEN)
print('''
     ██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗
     ██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝
     ██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░
     ██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░
     ██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗
     ╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
''')
print(Fore.RESET)


# Function to calculate total value of cards
def calculate_total(cards):
    total = 0
    ace_count = 0
    for card in cards:
        face = card[1]
        if face in ('K', 'Q', 'J'):
            total += 10
        elif face == 'A':
            ace_count += 1
            total += 11
        elif face == 'T':
            total += 10
        else:
            total += int(face)
    while total > 21 and ace_count:
        total -= 10
        ace_count -= 1
    return total


# Function to deal a card
def deal_card():
    import random
    return deck.pop(random.randint(0, len(deck) - 1))


# Initial deal for player and dealer
player_hand = [deal_card(), deal_card()]
dealer_hand = [deal_card(), deal_card()]

# Show initial hands
print("Player's Hand:", *player_hand)
print("Dealer's Hand:", dealer_hand[0], ", <Hidden>")

# Player's turn
while True:
    action = input("Hit or Stand? ").strip().lower()
    if action == "hit":
        player_hand.append(deal_card())
        print("Player's Hand:", *player_hand)
        if calculate_total(player_hand) > 21:
            print("Player busts! Dealer wins.")
            break
    elif action == "stand":
        break
    else:
        print("Invalid input. Please type 'hit' or 'stand'.")

# Dealer's turn
if calculate_total(player_hand) <= 21:
    print("Dealer's Hand:", *dealer_hand)
    while calculate_total(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        print("Dealer's Hand:", *dealer_hand)
        if calculate_total(dealer_hand) > 21:
            print("Dealer busts! Player wins.")
            break

# Determine the winner
if calculate_total(player_hand) <= 21 and calculate_total(dealer_hand) <= 21:
    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)
    if player_total > dealer_total:
        print("Player wins!")
    elif player_total < dealer_total:
        print("Dealer wins!")
    else:
        print("It's a tie!")
