import random
import os
import time
 
 # Personal Project: BlackJack Challenge 

# Creating the definition for a card
class Card:
    def __init__(original, suit, value, score_value):
         
        # Included suits for design and organization purposes
        original.suit = suit
 
        # Represents the letter values, like A for Ace, K for King, Q for Queen, etc.
        original.value = value
 
        # Represents the score values
        original.score_value = score_value
 
# Clear the terminal to help with organization for testing
def clear():
    os.system("clear")
 
# Function for displaying the cards 
def card_display(cards, hidden_from_player):
         
    s = ""
    for card in cards:
        s = s + "\t ________________"
        if hidden_from_player:
            s += "\t ________________"
    print(s)
 
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden_from_player:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|  {}            |".format(card.value)
        else:
            s = s + "\t|  {}             |".format(card.value)  
    if hidden_from_player:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden_from_player:
        s += "\t|      + +       |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden_from_player:
        s += "\t|    +     +     |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden_from_player:
        s += "\t|   +       +    |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden_from_player:
        s += "\t|   +       +    |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|       {}        |".format(card.suit)
    if hidden_from_player:
        s += "\t|          +     |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden_from_player:
        s += "\t|         +      |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden_from_player:
        s += "\t|        +       |"
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden_from_player:
        s += "\t|                |"
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden_from_player:
        s += "\t|                |"
    print(s)    
 
    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|            {}  |".format(card.value)
        else:
            s = s + "\t|            {}   |".format(card.value)
    if hidden_from_player:
        s += "\t|        +       |"        
    print(s)    
         
    s = ""
    for card in cards:
        s = s + "\t|________________|"
    if hidden_from_player:
        s += "\t|________________|"
    print(s)        
 
    print()
 
 
# Creating a function for single game of blackjack 
def blackjack_game(deck):
 
    # Array of cards for player and dealer 
    player_set_cards = []
    dealer_set_cards = []
 
    # Score variables for player and dealer 
    player_score = 0
    dealer_score = 0
 
    clear()
 
    # Initial dealing for player and dealer
    while len(player_set_cards) < 2:
 
        # Dealing a card (randomly)
        player_card = random.choice(deck)
        player_set_cards.append(player_card)
        deck.remove(player_card)
 
        # Incrementing the score value for the player
        player_score += player_card.score_value
 
        # If both the cards are Ace, make the first ace value 1
        if len(player_set_cards) == 2:
            if player_set_cards[0].score_value == 11 and player_set_cards[1].score_value == 11:
                player_set_cards[0].score_value = 1
                player_score -= 10
 
        # Basic printing of players cards and scores    
        print("Player cards: ")
        card_display(player_set_cards, False)
        print("Player score = ", player_score)
 
        input()
 
        # Dealing a card (randomly)
        dealer_card = random.choice(deck)
        dealer_set_cards.append(dealer_card)
        deck.remove(dealer_card)
 
        # Incrementing the score value for the dealer
        dealer_score += dealer_card.score_value
 
        # Print dealer cards and score
        # Hiding the second card and score 
        print("Dealer Cards: ")
        if len(dealer_set_cards) == 1:
            card_display(dealer_set_cards, False)
            print("Dealer score = ", dealer_score)
        else:
            card_display(dealer_set_cards[:-1], True)    
            print("Dealer score = ", dealer_score - dealer_set_cards[-1].score_value)
 
 
        # If both the cards are Ace, make the second ace value 1 
        if len(dealer_set_cards) == 2:
            if dealer_set_cards[0].score_value == 11 and dealer_set_cards[1].score_value == 11:
                dealer_set_cards[1].score_value = 1
                dealer_score -= 10
 
        input()
 
    # In the case the player gets a blackjack   
    if player_score == 21:
        print(" Player has a blackjack! Player wins!")
        quit()
 
    clear()
 
    # Printing the cards for dealer and player 
    print("Dealer Cards: ")
    card_display(dealer_set_cards[:-1], True)
    print("Dealer Score = ", dealer_score - dealer_set_cards[-1].score_value)
 
    print() 
 
    print("Player Cards: ")
    card_display(player_set_cards, False)
    print("Player Score = ", player_score)
 
    # Managing the players movement
    while player_score < 21:
        choice = input("Type in H to Hit or S to Stand: ")
 
        # Edge case/sanity check for user input for Hit or Stand 
        if len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S'):
            clear()
            print("Wrong choice! Try Again")
 
        # If player input H, deal a new car, update player score, and update player score to have ace
        if choice.upper() == 'H':
 
            player_card = random.choice(deck)
            player_set_cards.append(player_card)
            deck.remove(player_card)
 

            player_score += player_card.score_value
 
            # Updating player score in case player's card have ace in them
            c = 0
            while player_score > 21 and c < len(player_set_cards):
                if player_set_cards[c].score_value == 11:
                    player_set_cards[c].score_value = 1
                    player_score -= 10
                    c += 1
                else:
                    c += 1 
 
            clear()     
 
            # Printing the cards for player and dealers 
            print("Dealer Cards: ")
            card_display(dealer_set_cards[:-1], True)
            print("Dealer Score = ", dealer_score - dealer_set_cards[-1].score_value)
 
            print()
 
            print("Player Cards: ")
            card_display(player_set_cards, False)
            print("Player Score = ", player_score)
             
        # If player wants to stand, break
        if choice.upper() == 'S':
            break
 
 
    clear() 
 
    # Print the cards of players and dealers 
    print("Player cards: ")
    card_display(player_set_cards, False)
    print("Player score = ", player_score)
 
    print()
    print("Dealer reveals the cards....")
 
    print("Dealer cards: ")
    card_display(dealer_set_cards, False)
    print("Dealer score = ", dealer_score)
 
    # Checking if player has a blackjack
    if player_score == 21:
        print("Player has a blackjack!")
        quit()
 
    # If player wants to quit/lost
    if player_score > 21:
        print("Player lost. Game over!")
        quit()
 
    input() 
 
    # Managing the movement for dealers moves
    while dealer_score < 17:
        clear() 
 
        print("Dealer decides to hit.....")
 
        # Dealing card for dealer
        dealer_card = random.choice(deck)
        dealer_set_cards.append(dealer_card)
        deck.remove(dealer_card)
 
        # Incrementing the dealers score 
        dealer_score += dealer_card.score_value
 
        # Updating player score in case player's card have ace in them
        c = 0
        while dealer_score > 21 and c < len(dealer_set_cards):
            if dealer_set_cards[c].score_value == 11:
                dealer_set_cards[c].score_value = 1
                dealer_score -= 10
                c += 1
            else:
                c += 1
 
        # Printing the cards of player and dealer 
        print("Player Cards: ")
        card_display(player_set_cards, False)
        print("Player Score = ", player_score)
 
        print()
 
        print("Dealer Cards ")
        card_display(dealer_set_cards, False)
        print("Dealer Score = ", dealer_score)      
 
        input()
 
    # If the dealer loses
    if dealer_score > 21:        
        print("Dealer lost. You win!") 
        quit()  
 
    # In the case when a dealer gets a blackjack 
    if dealer_score == 21:
        print("Dealer has a blackjack! Player loses.")
        quit()
 
    # If its a tie game and scores match
    if dealer_score == player_score:
        print("Time Game! :)")
 
    # If the player wins 
    elif player_score > dealer_score:
        print("Player wins :)")                 
 
    # If the dealer wins 
    else:
        print("Dealer wins :)")                 
 
if __name__ == '__main__':
 
    # The different kinds of suits stored in an array 
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
 
    # The suit values- using the numeral representations of spades, hearts, clubs, and diamonds
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
 
    # the different kinds of cards 
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
    # card values stored in an array 
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
 
    # the deck of cards set to an array
    deck = []
 
    # setting a for loop to go through the suits 
    for suit in suits:
 
        # a for loop to go through all the cards 
        for card in cards:
 
            # appending all the components into the card class
            deck.append(Card(suits_values[suit], card, cards_values[card]))
     
    blackjack_game(deck)  
