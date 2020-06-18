import random

suits = ('Hearts','Diamonds','Clubes','Spades')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return 'The deck has : '+ deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  #For ace card having values 11 or 1 (changing)
        
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        #For tracing Ace card
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        # if total value > 21 and I still have an Ace
        # Than change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces > 0 :
            self.value -= 10
            self.aces -= 1
            
class Chips:
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet
    
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("How many chips are you going to bet?"))
        except:
            print('Sorry, Please provide a number!')
        else:
            if chips.bet > chips.total:
                print("Sorry,you do not have that much chips! You have: {}".format(chips.total))
            else:
                break

def hit(deck,hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    

def hit_or_stand(deck,hand):
    global playing  #to control an upcoming while loop
    
    while True:
        x = input('Hit or Stand? Enter h or s ')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn.")
            playing = False
            
        else :
            print("Sorry, Invalid choise! Please enter h or s..")
            continue
        
        break
        
        
# Functions to show player cards
def show_some(player,dealer):
    print("\nDealer's Hand: ")
    print(" < card hidden >")
    print('',dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep = '\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep ='\n ')
    print("Player's Hand =", player.value)
        
def player_bursts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_bursts(player,dealer,chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! PUSH.")


while True:
    
    #printing a opening statement 
    print("WELCOME TO BLACKJACK!...By Masud Ansari!")
    
    #creating & shuffling the deck, dealing two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    #Set up player's chips
    player_chips = Chips()
    
    take_bet(player_chips)
    
    #show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:
        # Choise for player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keeping one dealer's card hidden)
        show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            player_bursts(player_hand,dealer_hand,player_chips)
            
            break
            
    # If Player hasn't bursted, play Dealer's untill Dealer reaches half less than half of Player's
    if player_hand.value <= 21:
        
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)
            
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        #Different winning Scenarios
        if dealer_hand.value > 21:
            dealer_bursts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
            
            
            
    # To inform the Player of their chips total
    print('\n Player total chips are at: {}'.format(player_chips.total))
    
    # Asking player to play again
    new_game = input("would you like to play another round? y/n")
    
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing..!")
        break
    
    