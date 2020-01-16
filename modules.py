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
        return f'{self.figure} of {self.color}'


class Deck:
    FIGURES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    COLORS = ['heart', 'spades', 'diamonds', 'clubs']

    def __init__(self, num_of_decks=1):
        self.cards = []
        for i in range(num_of_decks):
            for color in self.COLORS:
                for figure in self.FIGURES:
                    self.cards.append(Card(figure, color))


if __name__ == '__main__':
    deck = Deck()
    for card in deck.cards:
        print(card)
    print(len(deck.cards))
