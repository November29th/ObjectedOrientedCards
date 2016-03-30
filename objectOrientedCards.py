from random import*

class Card(object):
    def __init__(self, suit = None, value = None):
        self.value = value

class Diamond(Card):
    def __init__(self):
        super(Diamond, self).__init__("Diamond", 4)

class Heart(Card):
    def __init__(self):
        super(Heart, self).__init__("Heart", 3)

class Club(Card):
    def __init__(self):
        super(Club, self).__init__("Club", 2)

class Spade(Card):
    def __init__(self):
        super(Spade, self).__init__("Spade", 1)


class SuitGame(object):
    """Contain methods for playing suit game"""

    def __init__(self):
        self.cards = []

    def populate_deck(self):

        self.cards +=  [Diamond() for i in range(13)]
        self.cards +=  [Spade() for i in range(13)]
        self.cards +=  [Heart() for i in range(13)]
        self.cards +=  [Club() for i in range(13)]

        return self.cards

    def remove_card(self, card):

        if card in self.cards:
            self.cards.remove(card)

        return self.cards


    def deal_hand(self):
        """Returns a list of 4 randomly picked cards from our cards list"""
        # initialize a new card list
        new_cards = []
        for i in range(4):
            index = randint(0,51)
            new_card = self.cards[index]
            self.remove_card(new_card)

            new_cards.append(new_card)

        return new_cards

    def calculate_score(self):
        """returns calculated value of cards"""
        new_cards = self.deal_hand()
        values = [c.value for c in new_cards]

        print values

        score = sum(values)

        print score
        return score



deck = SuitGame()
deck.populate_deck()
deck.deal_hand()
deck.calculate_score()


