# BlackJack Game

# Importing libraries -- used for shuffling cards
import random

# Boolean type to know whether play is in hand
playing = False

# Amount for buy-in
chip_pool = 100 
print('Your buy-in amount is:', chip_pool)

bet = 1

restart_phrase = "Press 'd' to deal the cards again, or press 'q' to quit."

# Card suits and ranks
suits = ('H', 'D', 'S', 'C')
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# Card values
card_val = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

# Card Class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def grab_suit(self):
        return self.suit

    def grab_rank(self):
        return self.rank

    def draw(self):
        print(self.suit + self.rank)

# Hand Class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False  # Ace logic

    def __str__(self):
        hand_comp = ""
        for card in self.cards:
            hand_comp += " " + card.__str__()
        return 'The hand has: {}'.format(hand_comp)

    def card_add(self, card):
        self.cards.append(card)
        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]

    def calc_val(self):
        if self.ace and self.value < 12:
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):
        if hidden and playing:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()

# Deck Class
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranking]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

# Functions for gameplay
def make_bet():
    global bet
    bet = 0
    print('What amount of chips would you like to bet? (Enter a whole number)')
    while bet == 0:
        try:
            bet_comp = int(input())
            if 1 <= bet_comp <= chip_pool:
                bet = bet_comp
            else:
                print(f"Invalid bet. You have {chip_pool} remaining.")
        except ValueError:
            print("Please enter a valid integer.")

def deal_cards():
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet
    deck = Deck()
    deck.shuffle()
    make_bet()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())
    result = "Hit or Stand? Press 'h' for hit or 's' for stand."
    playing = True
    game_step()

def hit():
    global playing, chip_pool, result, bet
    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())
        print("Player's hand:", player_hand)
        if player_hand.calc_val() > 21:
            result = 'Busted!' + restart_phrase
            chip_pool -= bet
            playing = False
    else:
        result = "Sorry, can't hit." + restart_phrase
    game_step()

def stand():
    global playing, chip_pool, result, bet
    while dealer_hand.calc_val() < 17:
        dealer_hand.card_add(deck.deal())
    if dealer_hand.calc_val() > 21:
        result = 'Dealer busts! You win!' + restart_phrase
        chip_pool += bet
    elif dealer_hand.calc_val() < player_hand.calc_val():
        result = 'You beat the dealer! You win!' + restart_phrase
        chip_pool += bet
    elif dealer_hand.calc_val() == player_hand.calc_val():
        result = 'It\'s a tie!' + restart_phrase
    else:
        result = 'Dealer wins!' + restart_phrase
        chip_pool -= bet
    playing = False
    game_step()

def game_step():
    print("\nPlayer's Hand:", player_hand)
    print("Player's Hand Value:", player_hand.calc_val())
    print("\nDealer's Hand:")
    dealer_hand.draw(hidden=True if playing else False)
    if not playing:
        print("Dealer's Hand Value:", dealer_hand.calc_val())
        print(f"Chip Total: {chip_pool}")
    print("\n", result)
    player_input()

def game_exit():
    print('Thanks for playing!')
    exit()

def player_input():
    plin = input("Enter 'h' to hit, 's' to stand, 'd' to deal, or 'q' to quit: ").lower()
    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        game_exit()
    else:
        print("Invalid input. Please try again.")
        player_input()

def intro():
    print("Welcome to BlackJack! Try to get as close to 21 as possible without going over!")
    print("Dealer hits until reaching 17. Aces count as 1 or 11.\n")

# Start the game
if __name__ == "__main__":
    intro()
    deal_cards()
