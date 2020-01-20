class Card:
    def __init__(self, figure, color):
        self.figure = figure
        self.color = color

    @property
    def value(self):
        if self.figure in ['K', 'Q', 'J']:
            return 10
        elif self.figure in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            return int(self.figure)
        elif self.figure == 'A':
            return 1, 11

    def __str__(self):
        return f'{self.figure}{self.color}'


class Deck:
    FIGURES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    COLORS = ['\u2661 (hearts)', '\u2660 (spades)', '\u2666 (diamonds)', '\u2667 (clubs)']

    def __init__(self, num_of_decks=1):
        self.cards = []
        for i in range(num_of_decks):
            for color in self.COLORS:
                for figure in self.FIGURES:
                    self.cards.append(Card(figure, color))


class Player:
    def __init__(self):
        self.hand = []
        self.hand_2 = []
        self.bet = 0
        self.bet_2 = 0
        self.bank = 0

    def deposit_money(self, amount):
        self.bank += amount

    def draw_card(self, deck, hand=None):
        if hand is None:
            hand = self.hand
        top_card = deck.pop()
        hand.append(top_card)

    def split(self):
        self.hand_2.append(self.hand.pop())
        self.bet_2 = self.bet

    def double(self, bet=None):
        if bet is None:
            self.bet += self.bet
            self.bank -= self.bet
        else:
            self.bet_2 += self.bet_2
            self.bank -= self.bet_2

    @staticmethod
    def count_hand_value(hand):
        ret_val = 0
        num_of_aces = 0
        for card in hand:
            if card.figure != 'A':
                ret_val += card.value
            else:
                num_of_aces += 1
        if num_of_aces != 0:
            while num_of_aces > 1:
                ret_val += 1
                num_of_aces -= 1
            if ret_val + 11 > 21:
                ret_val += 1
            else:
                ret_val += 11
        return ret_val

    @property
    def hand_value(self):
        return self.count_hand_value(self.hand)

    @property
    def hand_2_value(self):
        return self.count_hand_value(self.hand_2)


if __name__ == '__main__':
    deck = Deck()
    for card in deck.cards:
        print(card)
    print(len(deck.cards))
