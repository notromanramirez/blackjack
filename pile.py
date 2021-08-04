# Roman Ramirez
# rr8rk@virginia.edu

### IMPORT ###

from card import Card
from random import shuffle

# defines the Pile class, which extends from list
class Pile(list):
	# method: shuffle, shuffles the pile
	def shuffle(self):
		shuffle(self)

	# method: add, add a card to the pile
	def add(self, card: Card) -> None:
		self.append(card)

	# method: draw, pull a card from other and add to hand
	# hand.draw(deck)
	def draw(self, other) -> None:
		self.add(other.pop(0))

	# method: total, return the total of the pile: a sum of card values
	def total(self) -> int:

		total = sum([c.value for c in self])

		while (total > 21) and (11 in [c.value for c in self]):
			self[[c.value for c in self].index(11)].value = 1
			total = sum([c.value for c in self])
		
		return total

	# method: strHidden, shows a hidden version of the hand
	def strHidden(self) -> str:
		retVal = "["
		for c in self:
			if self.index(c) == (len(self) - 1):
				retVal += Card.X + Card.X + ", "
			else:
				retVal += str(c) + ", "
		retVal = retVal[:-2]
		retVal += "]"
		return retVal

	# magic method override: str, print a pile
	def __str__(self) -> str:
		retVal = "["
		for c in self:
			retVal += str(c) + ", "
		retVal = retVal[:-2]
		retVal += "]"
		return retVal

	# magic method override: init
	def __init__(self):
		super().__init__()

# defines the Deck class, extends from the Pile class.
class Deck(Pile):
	# magic method override: int
	def __init__(self):
		# calls the Pile's init magic method
		super().__init__()
		# add every card in a standard 52-card deck.
		for s in Card.SUITS:
			for n in Card.NUMBERS:
				self.add(Card(s, n))

# defines the Hand class, extends from the Pile class.
class Hand(Pile):

	# class attributes
	FOLD = 'fold'
	HIT = 'hit'
	STAND = 'stand'
	HOLD = 'hold'
	QUIT = 'quit'

	# provides a list of actions the player can make during the game
	def actionsList(self):
		actions = [Hand.FOLD]
		if self.total() <= 21:
			actions.append(Hand.HIT)

		if len(self) == 2:
			actions.append(Hand.STAND)
		else:
			actions.append(Hand.HOLD)

		return actions

	# method method override: init
	def __init__(self):
		# calls the Hand's init magic method
		super().__init__()
