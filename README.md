                                               BlackJack Application

This program is a terminal-based BlackJack game which was written in Python. The main objective of the game is to beat the dealer or the hands given by the card. This can be done in the following ways: 
Get 21 points on the players first two cards without the dealer having a blackjack
Reach a final score than the dealer without exceeding 21 
Letting the dealer draw additional cards until their hand can exceed 21 

The program is implemented with a deck of cards with two actions: Hit or Stand. The Hit (H) would allow the player to take another card from the dealer and the Stand (S) implies that the player takes no more cards and the dealer draws the card. 

**Instructions**
The code is stored in the file BJ.py. It can be run on Visual Studio Code, or any IDE/application that can run a python program. As usual, you can then save the file, compile, and run the code. For instance, if you are using Visual Studio Code, you can compile and run by stating: python3 BJ.py. With that, you can start playing BlackJack. Thank you for taking the time to review my program and my application. Hope you have fun! 

What Went Well
	In the allocated time, I managed to code most of the edge cases that would be involved in this program. This includes some sanity checks and not taking into account alternate user inputs at unnecessary points during the program. 
	Additionally, I found that I did a great job organizing the methods and laying out my ideas on a UML diagram before I began coding. Although suits were not required in the coding challenge document, I thought it was a choice that helped with organizing my data, as it made the organization process for appending to a card a little easier. 

Design Choices 
	As for design choices, I used 3 methods to organize my code, as described below. 
Displaying the cards
Running through a single game of blackjack. I then call the method at the end of the program for the algorithm to keep running 
A class card where I define the components I use for each card method 
	Additionally, I tried to recreate a card on the terminal for a better user experience. In hindsight, this might have not been the best way to spend my time on writing this program, but it created an extra visual element for the player. 

Algorithm Choices 
	I used a lot of if statements in the program because it was generally a pretty straightforward program. I did use for-loops for designing the card layout through the terminal. Additionally, I used another for-loop to append all the suits, card values onto the cards by using the append() method. I also used a while-loop to help keep track of the player and dealer's scores, specifically in the case when the player's card has an ace in them. Depending on the scenario, I increment the values by 1 or 11. 

Ace Card Scenario: 

Besides these three forms to help with my project flow, I placed the input() method in my program just to prevent my program from crashing. When it comes to data structures, I chose to use arrays to store the different values because of time purposes and simplicity. In the case when I had more time, I would have used a hash table for a better runtime for my algorithm. This was the case for storing the deck of cards, the players and dealers cards, and the point values for the cards. 


Extra Time 
	As always, there is always room for improvement for the code that I draft. If I had more time, I would have focused more on the user experience elements (better designs for the cards on the terminal or create a GUI). I would have also implemented a data structure that can result in a better runtime for the algorithm, just so that it can stand through several test cases. I would have also used less if-statements because while it was an easy way to account for specific cases, I could have thought of a solution that was a little less redundant. My current code repeats the if-statements for the players and the dealer, leaving it a little redundant for a code review. 
	Additionally, I would have written my own test cases and tested my program more if I has extra time to make it robust. 

