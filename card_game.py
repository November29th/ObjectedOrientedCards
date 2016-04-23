
#
# Your previous Plain Text content is preserved below:
#
# This is just a simple shared plaintext pad, with no execution capabilities.
#
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
#
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/profile
#
# Enjoy your interview!
#
#
from random import*

class Card(object):
    def __init__(self, suit = None, value = None):
        self.value = value
        # want thirteen values for each type of card.


class Diamond(Card):
    def __init__(self, value):
        super(Diamond, self).__init__("Diamond", value)

    def __repr__(self):
        """return representation for diamond object"""
        return "%d of Diamonds" %(self.value)


class Heart(Card):
    def __init__(self, value):
        super(Heart, self).__init__("Heart", value)

    def __repr__(self):
        """return representation for hear object"""
        return "%d of Hearts" %(self.value)

class Club(Card):
    def __init__(self, value):
        super(Club, self).__init__("Club", value)

    def __repr__(self):
        """return representation for diamond object"""
        return "%d of Clubs" %(self.value)


class Spade(Card):
    def __init__(self, value):
        super(Spade, self).__init__("Spade", value)

    def __repr__(self):
        """return representation for spade object"""
        return "%d of Spades" %(self.value)

# 0. Both players start with 50 coins.
# 1. Dealer plays two cards on the table (river cards)
# 2. Dealer deals two cards to both players (hands)
# 3. To play, players put 5 coin ante
# 4. Player 1 can either (a) fold (b) replace card (c) draw new card and add 2-3 coins to table (up to 2 times for replace/draw)
#    (d) claim you have the sum (x coin raise), in which case, they can call the bluff/match the bet, or fold
#    (e) Player can have from 2-4 cards by the end of the round.
# 5. Continue playing.
# 6. At the end of each round, both players reveal their cards. Whichever player has the closest value to the sum on the table, wins the pot. If both players have values equidistant to the sum, then the pot gets split in half between the players.
# 7. The game really ends when one player has 50 coins, and the other player has lost all their coins.


#TODO
#player class
#    coins, hand array,
# hand class.
    # hand.replaceCount
    # hand.drawCount
    # hand.score
    # hand.cards
    # deal hand function
        ## takes something from the deck.
    # actions
        ## draw a card
        ## replace a card
        ## have the sum
# class that will play the game.

class Player(object):
    """Represents a player"""

    def __init__(self, p_hand = None, coins = 50, play_count = 0):
        if p_hand is None:
            self.p_hand = Hand()
        else:
            self.p_hand = p_hand

        self.coins = coins
        # self.play_count = play_count


    def replace_card(self, index, game):

        # removes specified item from the array by index, and replaces it with another card
        del self.p_hand.cards[index]
        self.draw_card(game.cards, game)
        game.pot += 5
        self.coins -=5

    def draw_card(self, deck, game):

        new_card = deck[randint(0, 51)]
        self.p_hand.cards.append(new_card)
        game.pot += 5
        self.coins -=5
        return new_card



class Hand(object):
    """Represents hand for each player"""
    def __init__(self, score = 0, cards = None):

        # assert isinstance(cards, list)
        #     print "cards must be a list!"
        self.score = score
        if cards is None:
            self.cards = []
        else:
            self.cards = cards



    def calculate_score(self):
        """Calculating the sum of the hand for each player."""
        self.score = 0
        for card in self.cards:
            self.score += card.value

# class Round(object):
#     """"""

#     def __init__(self, )

# Round class?
##    While player still have coins
##    Pot
##    Once the pot has 10 coins, go to next round.
##


class SuitGame(object):
    """Contain methods for playing suit game"""

    def __init__(self):
        self.cards = []
        self.pot = 0

    def populate_deck(self):

        self.cards +=  [Diamond(i) for i in range(1,14)]
        self.cards +=  [Spade(i) for i in range(1,14)]
        self.cards +=  [Heart(i) for i in range(1,14)]
        self.cards +=  [Club(i) for i in range(1,14)]

        return self.cards

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)

        return self.cards


    def deal_hand(self, player):
        """Returns a list of 2 randomly picked cards from our cards list"""
        # initialize a new card list
        for i in range(2):
            length = len(self.cards)-1
            print length
            index = randint(0, length)
            new_card = self.cards[index]
            self.remove_card(new_card)

            player.p_hand.cards.append(new_card)
            player.p_hand.calculate_score()

        return player.p_hand.cards

    def show_sum(self, river_sum, player_1, player_2):
        """Give pot to the winner, and re-initialize value of pot to 0"""
    # on the playCount 3
    # whichever player has the sum closest to the rivercard sum wins.
    # if player1 has a score closer to the sum than player2, then player1 wins the pot. Otherwise player2.
        final_decision_1 = abs(river_sum - player_1.p_hand.score)
        final_decision_2 = abs(river_sum - player_2.p_hand.score)
        if final_decision_1 < final_decision_2:
            player_1.coins += self.pot
            print "Player 1 wins!"
        elif final_decision_1 > final_decision_2:
            player_2.coins += self.pot
            print "Player 2 wins!"
        else:
            player_1.coins += self.pot/2
            player_2.coins += self.pot/2
            print "It was a tie! Split the pot!"
        self.pot = 0



def main():
    """initializes the game"""

    # instantiate three player objects
    Game = SuitGame()
    Game.populate_deck()

    # initializes players
    Player1 = Player()
    Player2 = Player()
    Dealer = Player()
    x=1

    # while Player1.coins > 0 and Player2.coins > 0 and len(Game.cards) >=6:
    while x == 1:
        # first, we deal the hands to the players
        # we give the players the choice as to what they want to do.

        # two hands of the players, and the river hand.
        play_count = 0

        Game.deal_hand(Player1)
        Game.deal_hand(Player2)
        Game.deal_hand(Dealer)

        river_sum = Dealer.p_hand.score

        while play_count < 2:

            # ante
            Player1.coins -= 5
            Player2.coins -= 5
            Game.pot += 10

            # actions
            action1 = raw_input("Player1: What is your next move? Enter 1 to draw a new card, 2 to replace a card")
            if action1 == "1":
                drawn = Player1.draw_card(Game.cards, Game)
                print drawn
            elif action1 == "2":
                print Player1.p_hand.cards
                index = raw_input("Enter an index to replace between 0 and " + str((len(Player1.p_hand.cards) - 1)))
                Player1.replace_card(int(index), Game)


            action2 = raw_input("Player2: What is your next move? Enter 1 to draw a new card, 2 to replace a card")
            # fold, claim

            if action2 == "1":
                drawn = Player2.draw_card(Game.cards, Game)
                print drawn
            if action2 == "2":
                print Player2.p_hand.cards
                index = raw_input("Enter an index to replace between 0 and " + str((len(Player2.p_hand.cards) - 1)))
                Player2.replace_card(int(index), Game)

            # after both players make a round, we incremenet play count.
            play_count += 1;
        Game.show_sum(river_sum, Player1, Player2)
        x += 1



main()
    # drawn_card = Player.draw_card(self.cards)
    # self.remove_card(drawn_card);
#     def calculate_score(self):
#         """returns calculated value of cards"""
#         new_cards = self.deal_hand()
#         values = [c.value for c in new_cards]

#         print values
#         score = sum(values)

#         print score
#         return score



# deck = SuitGame()
# deck.populate_deck()
# deck.deal_hand()
# deck.calculate_score()

# player = Player()

# print player.coins