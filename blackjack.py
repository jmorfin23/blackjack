from IPython.display import clear_output
from random import randint
#TODO:

#steps:
#1.
#2.

class blackJack():

    def __init__(self):
        pass
    def decorator(self, f):
        print('–––––––––')
        f()
        print('–––––––––')
    def instructions(self):
        clear_output()
        print('–––––––––– How to Play ––––––––––')
        print(' ')
        print('The game is based on points.')
        print('The goal of the game is to get to 21 points.')
        print('Face cards are worth 10 points.')
        print('Numbered cards are worth their value.')
        print('Aces are worth 1 or 11, whichever you choose')
        print(' ')
        print('Player plays against the dealer.')
        print('Each player is dealt two cards but only 1 card of the dealer\'s is faced up.')
        print('After you get dealt cards, you can get dealt another to add to your cards if you wish.')
        print('You can either \'hit\' or \'stay\', hit means you want another card, stay means you do not want another card.')
        print('The player with the lowest cards that is closest to 21 wins.')

    def gameLoop(self, player, dealer):
        print(dealer.getCards())
        print(dealer.getCards())
        print('––––––')
        print(player.getCards())
        print(player.getCards())
        print('––––––')







class Player():

    def __init__(self, name = 'player'):
        self.name = name

    #returns 2 random cards for the players hand
    def getCards(self):
        number = randint(1,13)
        suit = randint(1,4)
        return  number, suit

class Dealer():

    def __init__(self):
        pass

    #returns 2 random cards for the dealers hand
    def getCards(self):
        number = randint(1,13)
        suit = randint(1,4)
        if number == 1:
            return 'A'
        if number == 11:
            return 'J'
        if number == 12:
            return 'Q'
        if number == 13:
            return 'K'
        else:
            return number

        if suit == 1:
            return '♦︎'
        if suit == 2:
            return '♥︎'
        if suit == 3:
            return '♣︎'
        if suit == 4:
            return '♠︎'
        else:
            print('invalid')

# ----------- main calling section -----------

print('Welcome to BlackJack!')
print(' ')
print('Press enter to play, quit to exit, or i for instructions on how to play. ')


while True :
    #for game loop
    playing = True

    #creating instances
    bj = blackJack()
    player = Player()
    dealer = Dealer()

    question = input('What would you like to do? ').lower()

    if question == 'quit':
        break
    elif question == 'i':
        bj.instructions()
    else:
        clear_output()
        while playing:
            bj.gameLoop(player,dealer)

            print('Hit or Stay?')
            print(' ')
            question = input('What would you like to do? ').lower()
            clear_output()

            #base case
            if question == 'quit':
                playing = False
                print('Thanks for playing.')
