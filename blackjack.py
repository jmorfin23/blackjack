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
        print('–––––––––– How to Play BlackJack ––––––––––')
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

    def gameLoop(self, player, dealer, question):

        clear_output()
        if question == 'hit':
            print('Players\'s Cards:')
            print('–––––––––––––––')
            player.dealCards()
            print('Points: ')
            player.addPoints()
            print(player.getPoints())
            print('–––––––––––––––')
            print(' ')
            print('Dealer\'s Cards:')
            print('–––––––––––––––')
            print(dealer.showCards())
            return

        print('Players\'s Cards:')
        print('–––––––––––––––')
        player.dealCards()
        print('–––––––––––––––')
        print(' ')
        print('Points: ')
        player.addPoints()
        print(player.getPoints())

        print(' ')
        print('Dealer\'s Cards:')
        print('–––––––––––––––')
        print(dealer.dealCards())
        print('–––––––––––––––')
        dealer.addPoints()





    #checks if cards are the same
    def checkSameCards(self, obj1, obj2):
        for i in range(len(player.cards)):
            if obj1.cards[i] in obj2.cards:  #condensing this later
                return True
            if obj2.cards[i] in obj1.cards:
                return True
            return

    def playerBlackJack(self):
        print('Congrats you\'ve got blackjack!')
        return
    def playerWin(self):
        print('Congrats you\'ve beat the dealer!')
        return

    def playerLose(self):
        print('Sorry, you went over 21. You lost.')
        return
    def dealerLose(self):
        print('The dealer went over 21. You\'ve won!')
        return
    def dealerWin(self):
        print('The dealer won!')
        return
    def tieGame(self):
        print('You tied!')
        return
class Player():

    def __init__(self, cards = [], name = 'player', points = 0):
        self.name = name
        self.cards = cards
        self.points = points
        self.addpoints = []

    def getPoints(self):
        return self.points
    def addPoints(self):
        self.addpoints = []
        for i in range(len(self.cards)):
            if self.cards[i][0] == 'J':
                self.addpoints.append(10)
            elif self.cards[i][0] == 'Q':
                self.addpoints.append(10)
            elif self.cards[i][0] == 'K':
                self.addpoints.append(10)
            elif self.cards[i][0] == 'A':
                self.addpoints.append(11)
            else:
                self.addpoints.append(self.cards[i][0])
        self.points = sum(self.addpoints)

    def showCards(self):
        return player.cards

    def getCards(self):
        return self.cards

    #returns 2 random cards for the players hand
    def dealCards(self):
        number = randint(1,13)
        suit = randint(1,4)

        #setting conditions for face cards
        if number == 1:
            number = 'A'
        if number == 11:
            number = 'J'
        if number == 12:
            number = 'Q'
        if number == 13:
            number = 'K'
        if suit == 1:
            suit = '♦︎'
        if suit == 2:
            suit = '♥︎'
        if suit == 3:
            suit = '♣︎'
        if suit == 4:
            suit = '♠︎'
        if [number, suit] not in self.cards:
            self.cards.append([number, suit])
            return print(self.cards)
        else:
            print('Sorry, the same card was dealt. Deal again.')
            #calls deal cards again to get another card
#             self.addpoints = []
            player.dealCards()

class Dealer():

    def __init__(self, cards = [], name = 'dealer', points = 0):
        self.cards = cards
        self.name = name
        self.points = points
        self.addpoints = []

    def getPoints(self):
        return self.points
    def addPoints(self):
        self.addpoints = []
        for i in range(len(self.cards)):
            if self.cards[i][0] == 'J':
                self.addpoints.append(10)
            elif self.cards[i][0] == 'Q':
                self.addpoints.append(10)
            elif self.cards[i][0] == 'K':
                self.addpoints.append(10)
            elif self.cards[i][0] == 'A':
                self.addpoints.append(11)
            else:
                self.addpoints.append(self.cards[i][0])
        self.points = sum(self.addpoints)
    def showCards(self):
        return dealer.cards

    def getCards(self):
        return self.cards
    #returns 2 random cards for the dealers hand
    def dealCards(self):
        number = randint(1,13)
        suit = randint(1,4)

        #setting conditions for face cards
        if number == 1:
            number = 'A'
        if number == 11:
            number = 'J'
        if number == 12:
            number = 'Q'
        if number == 13:
            number = 'K'
        if suit == 1:
            suit = '♦︎'
        if suit == 2:
            suit = '♥︎'
        if suit == 3:
            suit = '♣︎'
        if suit == 4:
            suit = '♠︎'
        if [number, suit] not in self.cards:
            self.cards.append([number, suit])
            return self.cards[0]
        else:
            #calls deal cards again to get another card
#             self.addpoints = []
            dealer.dealCards()



# ----------- main calling section -----------

print('Welcome to BlackJack!')
print(' ')
print('Press enter to play, quit to exit, or i for instructions on how to play. ')

active = True
while active:

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
            bj.gameLoop(player,dealer, question)


            #if cards are the same deal again
            if bj.checkSameCards(player, dealer):
                #this takes away cards and give new cards
                player.cards.pop()
                dealer.cards.pop()
                continue

            #check if it is the start of the game to deal 2 cards first
            if len(player.cards) < 2:
                continue

            #checking if player wins
            if player.points == 21:
                bj.playerBlackJack()
                break

            #checking if you bust
            if player.points > 21:
                bj.playerLose()
                break
            #dont know if this is the best spot for this
            if dealer.points < 17:
                dealer.dealCards()
                dealer.addPoints()


            print(' ')
            print('Hit or Stay?')
            print(' ')
            question = input('What would you like to do? ').lower()

            #when player stays, win / lose conditions are checked.
            if question == 'stay':
                clear_output()
                print('Players\'s Cards:')
                print('–––––––––––––––')
                print(player.showCards())
                print('Points: ')
                player.addPoints()
                print(player.getPoints())
                print('')
                print('Dealers\'s Cards:')
                print('–––––––––––––––')
                print(dealer.showCards())
                print('Points: ')
                dealer.addPoints()
                print(dealer.getPoints())
                print(' ')

                if player.points > dealer.points and player.points < 21:
                    bj.playerWin()
                    break
                elif player.points == dealer.points:
                    bj.tieGame()
                    break
                elif dealer.points > 21:
                    bj.dealerLose()
                    bj.playerWin()
                    break
                else:
                    bj.dealerWin()
                    break


            #base case
            if question == 'quit':
                playing = False
                active = False
                print('Thanks for playing.')

    #checks if player would like to play again
    question = input('Would you like to play again?').lower()

    if question == 'no':
        break
    else:
        #goes back to top and resets all variables
        break
