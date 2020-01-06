import random

# init global variables used for game
player = []
dealer = []

class Deck(object):
    def __init__(self,rank=[], suit=[], whole_deck=[], scrambled_deck=[]):
        self.rank = ['1','2','3','4','5','6','7','8','9','J','Q','K','A']
        self.suit = ['♠','♣','♥','♦︎︎']
        self.whole_deck = whole_deck
        self.scrambled_deck = scrambled_deck
        #construct deck from existing attributes
        def makedeck(self):
            self.whole_deck = []            
            i=0
            while i < 4:
                for r in self.rank:
                    self.whole_deck.append(r+self.suit[i])  
                i += 1
            return self.whole_deck
        self.whole_deck = makedeck(self)

    def draw_a_card(self):
        d=self.whole_deck.pop(random.choice(list(range(len(self.whole_deck)))))
        return d

class Game(Deck):
    def __init__(self,credit=100, bet=10):
        Deck.__init__(self)
        self.credit = credit
        self.bet = bet
    def getcredit(self):
        while True:
            try:
                self.credit = int(input("How many chips would you like to buy? "))
            except:
                print("You need to specify number")
                continue
            else:
                print(str(self.credit) + ' Chips Purchased')
                print("Have fun!")
                break
        return self.credit
    def makebet(self):
        while True:
            try:
                self.bet = int(input("How much do you want to bet? "))
            except:
                print("You need to specify number")
                continue
            if self.bet > self.credit:
                print('You can\'t bet more than you have credit')
                continue
            else:
                print('You are betting ' + str(self.bet)) 
                break
    def deal(self, p_turn=0, d_turn=0):
        global dealer
        global player
        i = 0
        j = 0
        while i < p_turn:
            player.append(g.draw_a_card())
            i += 1
        while j < d_turn:
            dealer.append(g.draw_a_card())
            j += 1

def clear_screen():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

####################Construct Cards####################
def makecard(dealer, player, hidden=0):
    card =   ['╔═══════╗\t','║ {}     ║\t','║       ║\t','║   {}   ║\t','║       ║\t','║     {} ║\t','╚═══════╝\t']
    h_card = ['╔═══════╗\t','║▓▓▓▓▓▓▓║\t' ,'║▒▒▒▒▒▒▒║\t','║▓▓▓▓▓▓▓║\t' ,'║▒▒▒▒▒▒▒║\t','║▓▓▓▓▓▓▓║\t' ,'╚═══════╝\t']

    global player_cards
    player_cards = ['' for i in player]
    c=0
    p=0
    while p < len(player):
        for c in range(0, len(card)):
            alter = [1,0,0,1,0,0,1]
            current_card=[player[p][:1], player[p][1:]]
            player_cards[p] += str(card[c]).format(current_card[alter[c]])
        player_cards[p] = player_cards[p].split("\t")
        p += 1

    global dealer_cards
    dealer_cards = ['' for i in dealer]
    c=0
    p=0 

    while p < len(dealer):
        for c in range(0, len(card)):
            alter = [1,0,0,1,0,0,1]
            current_card=[dealer[p][:1], dealer[p][1:]]
            dealer_cards[p] += str(card[c]).format(current_card[alter[c]])
        dealer_cards[p] = dealer_cards[p].split("\t")
        p += 1

    if  hidden == 1:
        dealer_cards[1]=''.join(h_card)
        dealer_cards[1] = dealer_cards[1].split("\t")

def printcards(dealer_cards, player_cards):
    for i in range(len(dealer_cards[0])):
        for j in range(len(dealer_cards)):
            print('{}'.format(dealer_cards[j][i]), end=' ')
        print()

    for i in range(len(player_cards[0])):
        for j in range(len(player_cards)):
            print('{}'.format(player_cards[j][i]), end=' ')
        print()
####################Construct Cards END####################

def makerank(who):
    i=0
    player_rank = []
    while i < len(who):
        player_rank.append(who[i][0])

        for ii in player_rank:
            player_rank = [10 if ii=='K' or ii=='Q' or ii=='J' else ii for ii in player_rank]

        for ii in player_rank:        
            if ii == 'A':
                tmp_suit = player_rank.pop()
    #            tmp_suit = player_rank.pop(player_rank.index(ii))            
                if sum([ int(x) for x in player_rank]) <= 10:
                    tmp_suit = 11
                    player_rank.append(tmp_suit)
                elif sum([ int(x) for x in player_rank]) > 10:
                    tmp_suit = 1
                    player_rank.append(tmp_suit)
        i += 1         

    player_rank = [ int(x) for x in player_rank ]
    return sum(player_rank)

def newdeck(mindecksize):
    d = Deck()
    if len(g.whole_deck) < mindecksize: 
        g.whole_deck = d.whole_deck

def cards(z):
    if z == 0:
        makecard(dealer, player, 0)
        printcards(dealer_cards, player_cards)
    elif z == 1:
        makecard(dealer, player, 1)
        printcards(dealer_cards, player_cards)

def winlose(who):
    if who == 'p':
        g.credit = g.credit + g.bet
        print('You win!')
        print('Your credit is: ' + str(g.credit))
    elif who == 'd':
        g.credit = g.credit - g.bet
        print('Dealer wins!')
        print('Your credit is: ' + str(g.credit))       
    elif who == 'dr':
        print('Push')
        print('Your credit is: ' + str(g.credit))               

def dealerplay():
    while makerank(dealer) < 17:
        g.deal(0,1)

#Debug functions, can be removed at any time

def debug_printset():
    i=0
    while i < len(player):
        print(player[i])
        i += 1

# Functions end here
g = Game()

def play():
    d = Deck()
    global g
    global player
    global dealer
    i = 0
    clear_screen()
    g.getcredit()
    while True: #Whole game loop
        player = []
        dealer = []      
        g.deal(2,2)
        i += 1
        clear_screen()
        g.makebet()
        cards(1)
        newdeck(5)
        #########################Is it blackjack?#########################
        if makerank(player) == 21: 
            if i == 1 and makerank(dealer) != 21:
                print('Blackjack!')
                winlose('p')
                break
            elif i == 1 and makerank(dealer) == 21:
                winlose('dr')
                break
        #########################Is it blackjack? END#########################        
        while True: #hand loop              
            player_input = str(input("Press 'h' to hit, or 's' to stand \n"))
            if player_input == 'h':
                newdeck(1)
                g.deal(1)
                if makerank(player) > 21:
                    clear_screen()
                    cards(0)
                    print('Busted!')
                    winlose('d')
                    break
                elif makerank(player) < 21:
                    clear_screen()
                    cards(1)
                    continue
                elif makerank(player) == 21:
                    clear_screen()
                    cards(0)
                    dealerplay()
                    if makerank(dealer) == 21:
                        winlose('dr')
                        break
                    elif makerank(dealer) < 21:
                        winlose('p')
                        break

            elif player_input == 's':
                dealerplay()
                clear_screen()
                cards(0)
                if  makerank(dealer) > 21:
                    winlose('p')
                    break
                elif makerank(dealer) > makerank(player):
                    winlose('d')
                    break
                elif makerank(dealer) < makerank(player):
                    winlose('p')
                    break
                elif makerank(dealer) == makerank(player):
                    winlose('dr')
                    break
###############Gameover?####################
        if g.credit == 0:
            print("Game Over")
            exit()  
###############Play again?##################            
        while True: 
            print(len(g.whole_deck))
            print('press \'d\' to deal again, or \'c\' to close')
            deal = str(input())
            if deal == 'd':
                i -= 1
                break
            elif deal == 'c':
                print('Game ended. Your remaining credit is: ' + str(g.credit))
                exit()
            else:
                print("Incorrect input, please input 'd' to Deal again, 'c' to close the game")
                continue
###############Play again? END##################            

play()
