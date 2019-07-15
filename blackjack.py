from IPython.display import clear_output
from random import randint
#TODO: add currency and betting

class blackJack():

    def __init__(self):
        pass
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
            print(' ')
            print('Player\'s Bet: ' + str(player.currency_to_bet))
            print(' ')
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
            print(dealer.showFirst_Card())
            return

        print(' ')
        print('Player\'s Bet: ' + str(player.currency_to_bet))
        print(' ')
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
        print(f'Sorry, you went over 21. You lost: {player.currency_to_bet}')
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
    def playerAddBet(self, bet_to_add):
        player.bank = player.bank + bet_to_add

    def playerLoseBet(self,bet_lost):
        player.bank = player.bank - bet_lost

class Player():

    def __init__(self, cards = [], name = 'player', points = 0, bank = 1000):
        self.name = name
        self.cards = cards
        self.points = points
        self.bank = bank
        self.currency_to_bet = 0
        self.addpoints = []
    def enterName(self):
        question = input('Enter player name: ')
        self.name = question.title()

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


    def resetCards(self):
        self.cards = []

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
            player.dealCards()

class Dealer():

    def __init__(self, cards = [], name = 'dealer', points = 0):
        self.cards = cards
        self.name = name
        self.points = points
        self.addpoints = []

    def resetCards(self):
        self.cards = []

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
    def showFirst_Card(self):
        return dealer.cards[0]
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
            dealer.addPoints()





# ----------- main calling section -----------

print('Welcome to BlackJack!')
print(' ')
print('Press enter to play, quit to exit, or i for instructions on how to play. ')


active = True
#creating instances
bj = blackJack()
player = Player(cards = [], bank = 1000)
dealer = Dealer(cards = [])
player.enterName()
while active:

    #for game loop
    playing = True

    player.resetCards()
    dealer.resetCards()

    #i shouldnt have to do this it should automatically get reset?
#     print(dealer.cards)
#     print(player.cards)
#     print(player.bank)
    print(' ')
    print(f"Hi {player.name}!")
    print(' ')
    print(f'Player\'s Bank: {player.bank}')
    question = input('What would you like to do? ').lower()

    if question == 'quit':
        break
    elif question == 'i':
        bj.instructions()
        continue
    else:
        clear_output()
        print(f'Player\'s Bank: {player.bank}')
        money = int(input('How much would you like to bet? '))
        if money > player.bank:
            print('Sorry, you don\'t have enough money to bet that much.')
            print('')
            print('Please come back when you get more money.')
            break
        player.currency_to_bet = money
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
            #dont know if this is the best spot for this
            if dealer.points < 17:
                dealer.dealCards()
                dealer.addPoints()

            #checking if player wins
            if player.points == 21:
                bj.playerBlackJack()
                bj.playerAddBet(player.currency_to_bet)
                break

            #checking if you bust
            if player.points > 21:
                bj.playerLose()
                bj.playerLoseBet(player.currency_to_bet)
                break



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
                    bj.playerAddBet(player.currency_to_bet)

                    break
                elif player.points == dealer.points:
                    bj.tieGame()
                    break
                elif dealer.points > 21:
                    bj.dealerLose()
                    bj.playerWin()
                    bj.playerAddBet(player.currency_to_bet)
                    break
                else:
                    bj.dealerWin()
                    bj.playerLoseBet(player.currency_to_bet)
                    break


            #base case
            if question == 'quit':
                playing = False
                active = False
                print('Thanks for playing.')
    print(' ')
    print(f'Player\'s Bank: {player.bank}')
    #checks if player would like to play again
    question = input('Would you like to play again?').lower()

    if question == 'no':
        break
    else:
        #goes back to top and resets all variables? but this doesnt seem to work?
        clear_output()
