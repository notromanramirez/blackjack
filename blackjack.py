# Roman Ramirez
# rr8rk@virginia.edu

### CLASS IMPORTS ###

from card import Card
from pile import Pile
from pile import Deck
from pile import Hand

def main():

	### ONE-TIME INITIALIZATION ###

	credits: int = 5

	while credits > 0:

		### PER-TURN INITIALIZATION ###

		# initilizing the deck
		deck = Deck()
		deck.shuffle()

		# initializing empty hands
		hand, house = Hand(), Hand()
		# drawing from the deck 
		for _ in range(2):
			for d in (hand, house):
				d.draw(deck)

		### GAME ###

		# the wager is how much the player bets per turn before playing a game
		wager = -1
		# while the wager isn't valid
		while (wager < 0) or (wager > credits):
			print("You have %i credits." % credits)
			wager = input("How much do you want to wager? Or you can %s.\n" % ([Hand.QUIT]))
			# allows the player to quit before playing
			if wager == Hand.QUIT:
				exit()
			# checks for if the wager is an int
			elif not wager.isdigit():
				wager = -1
				print("\nYou must enter a number!")
			# bounds checking
			else:
				wager = int(wager)
				if wager <= 0:
					print("\nYou have to wager something!")
				elif wager > credits:
					print("\nYou can't wager %i credits!" % wager)

		print("\nYou wagered %i credits." % wager)

		# Player's Turn
		response = ""
		# while the player is continuing his turn
		while (hand.total() <= 21) and ((response != Hand.STAND) and (response != Hand.HOLD)):
			
			# display the current board
			print('')
			print('  You:', hand, hand.total())
			print('House:', house.strHidden())

			# display the current actions
			print("\nYou can %s." % str(hand.actionsList()))
			response = ""
			# valid response checking
			while response not in hand.actionsList():
				response = input("What would you like to do?\n")
				if response not in hand.actionsList():
					print("not valid")

			# code for the hit action
			if response == Hand.HIT:
				hand.draw(deck)

		# House's Turn
		while (house.total() <= 17):
			house.draw(deck)

		### RESULT ###

		# display the current board
		print("")
		print('  You:', hand, hand.total())
		print('House:', house, house.total())
		print("")

		playerVal = hand.total()
		houseVal = house.total()

		# result checking
		if (len(hand) == 2) and (Card.TEN not in [c.suit for c in hand]) and (hand.total() == 21):
			credits += wager * 2
			print("BlackJack!")
		elif playerVal > 21:
			credits -= wager
			print("You busted...")
		elif houseVal > 21:
			credits += wager
			print("The house busted.")
		elif playerVal < houseVal:
			credits -= wager
			print("The house wins.")
		elif playerVal == houseVal:
			print("A tie, you both push.")
		else:
			credits += wager
			print("You win!")

# run the main function if blackjack.py is run.
if __name__ == '__main__':
	main()