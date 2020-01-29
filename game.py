from modules import Deck, Player, player_turn
from random import shuffle
from validators import validate_pos_int
from time import sleep

welcome_message = '''
Welcome to blackjack!
In this game you'll play against the dealer.
In order to win, you need to get closer to 21 points than dealer, but you cannot exceed the 21 points margin.
Cards 2-10 has the value of a number, J, Q and K are all worth 10 points,
while A can be 1 or 11, whatever is better for the hand.
'''

print(welcome_message)

# prepare table
deck = Deck(num_of_decks=6)
deck = deck.cards
reshuffle = len(deck) * 0.75
shuffle(deck)
croupier = Player()

# prepare player
player = Player()
money = None
while not validate_pos_int(money):
    money = input('Deposit some money to begin: ')
money = int(money)
player.deposit_money(money)

cont = None
while cont != 'q':
    blackjack = False
    # initial bet
    bet = None
    while not validate_pos_int(bet):
        bet = input('Place your bet: ')
    bet = int(bet)
    if bet > player.bank:
        print('You cannot bet more than wou have!\nYour bet was set as `all in`.\n')
        bet = player.bank
    player.bet = bet
    player.bank -= bet

    # dealing cards
    for i in range(4):
        if i % 2 == 0:
            player.draw_card(deck)
        else:
            croupier.draw_card(deck)

    print(f'Croupiers hand: ?? {croupier.hand[1]}')
    player.print_hand(hand=player.hand)

    # blackjack
    if player.hand_value == 21:
        blackjack = True
        print('You got Blackjack!')
        sleep(3)
        print(f'Croupiers hand: ', end='')
        for card in croupier.hand:
            print(card, end='')
        print(f' Hand value: {croupier.hand_value}')
        if croupier.hand_value != 21:
            print('You won and the house is paying you 3 to 2 on your bet!')
            player.deposit_money(2.5 * player.bet)
        else:
            print('Draw')
            player.deposit_money(player.bet)
        player.bet = 0
    if not blackjack and croupier.hand_value == 21:
        blackjack = True
        croupier.print_hand()
        print(f'\nDealer has blackjack!\nYou lost!')
        sleep(3)
        player.bet = 0

    # split decision
    split_decision = None
    if not blackjack and player.hand[0].figure == player.hand[1].figure:
        while split_decision not in ['yes', 'no']:
            split_decision = input('Do you want to split your cards? [yes/no]\n')
        if split_decision == 'yes':
            split_decision = True
            player.split()
            player.draw_card(deck)
            player.draw_card(deck, hand=player.hand_2)
            player.print_hand(hand=player.hand)
            player.print_hand(hand=player.hand_2)
            print('\n')
            player.print_hand(hand=player.hand)
        elif split_decision == 'no':
            split_decision = False
            print('no changes')

    if not blackjack:
        # players turn
        player_turn(deck=deck, player=player, hand=player.hand)

        if split_decision:
            print('Second hand')
            player.print_hand(hand=player.hand_2)
            player_turn(deck=deck, player=player, hand=player.hand_2, bet=player.bet_2)

        # croupiers turn
        croupier.print_croupiers_hand()
        while croupier.hand_value < 17 and player.hand_value <= 21 and player.hand_2_value <= 21:
            croupier.draw_card(deck)
            croupier.print_croupiers_hand()
            sleep(1)

        # results
        if player.hand_value > 21:
            print('You busted!')
        elif croupier.hand_value > 21 or player.hand_value > croupier.hand_value:
            print('You won!')
            player.deposit_money(2 * player.bet)
        elif player.hand_value == croupier.hand_value:
            print('Draw')
            player.deposit_money(player.bet)
        else:
            print('You lost!')
        player.bet = 0
        if split_decision:
            print('Second hand result:')
            if player.hand_2_value > 21:
                print('You busted!')
            elif croupier.hand_value > 21 or player.hand_2_value > croupier.hand_value:
                print('You won!')
                player.deposit_money(2 * player.bet_2)
            elif player.hand_2_value == croupier.hand_value:
                print('Draw')
                player.deposit_money(player.bet_2)
            else:
                print('You lost!')
            player.bet_2 = 0

    # reset hands
    player.hand = []
    croupier.hand = []
    if player.bank == 0:
        print('You lost all your money!')
        break
    print(f'\nYour money: {player.bank}')
    print('Press q to exit the game or any other to continue')
    cont = input()

    if len(deck) <= reshuffle:
        print('Deck is being reshuffled')
        sleep(3)
        deck = Deck(num_of_decks=6)
        deck = deck.cards
        shuffle(deck)
