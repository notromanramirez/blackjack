# Roman Ramirez
# rr8rk@virginia.edu

### IMPORTS ###
from random import randint;

### defines the Card Class
class Card:

	# class attributes
	SUITS: list = ['H', 'D', 'C', 'S']
	H, D, C, S = SUITS
	NUMBERS: list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
	ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING = NUMBERS
	X = 'X'

	# returns the value of a given card based on their 'num'
	def calculateValue(self) -> int:
		if self.num.isdigit():
			return int(self.num)
		else:
			if self.num == Card.ACE:
				return 11
			else:
				return 10

	# override the str magic method
	def __str__(self) -> str:
		return "%s%s" % (str(self.suit), str(self.num))

	# override the init magic method
	# args: suit and num to set a specific suit and num
	def __init__(self, suit: str = None, num: int = None):
		# assign passed-in suit and num
		if suit and num:
			self.suit = suit
			self.num = num
		# assign random suit and num
		else:
			self.suit = Card.SUITS[randint(0, len(Card.SUITS) - 1)]
			self.num = Card.NUMBERS[randint(0, len(Card.NUMBERS) - 1)]

		# calculate the value of the card
		self.value = self.calculateValue()