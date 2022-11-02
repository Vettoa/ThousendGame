import random

class Thousend:

    def __init__(self, number_of_players=2):
        #Deck
        self.deck = ['Clubs 9', 'Clubs 10', 'Clubs Jack', 'Clubs Queen', 'Clubs King', 'Clubs Ace', 'Diamonds 9', 'Diamonds 10', 'Diamonds Jack', 'Diamonds Queen', 'Diamonds King', 'Diamonds Ace', 'Hearts 9', 'Hearts 10', 'Hearts Jack', 'Hearts Queen', 'Hearts King', 'Hearts Ace', 'Spades 9', 'Spades 10', 'Spades Jack', 'Spades Queen', 'Spades King', 'Spades Ace']
        random.shuffle(self.deck)

        #Players and points table
        self.number_of_players = number_of_players
        self.players1 = self.spread_of_cards()
        self.players2 = self.spread_of_cards()
        if self.number_of_players < 3:
            self.players_points = {'Player1': 0, 'Player2': 0}
        elif self.number_of_players == 3:
            self.players3 = self.spread_of_cards()
            self.players_points = {'Player1': 0, 'Player2': 0, 'Player3': 0}
        elif self.number_of_players == 4:
            self.players3 = self.spread_of_cards()
            self.players4 = self.spread_of_cards()
            self.players_points = {'Player1' : 0, 'Player2' : 0, 'Player3' : 0, 'Player4' : 0}

    def spread_of_cards(self): #Spread of cards
        player = []
        for x in range(1):
            if self.number_of_players == 2:
                for y in range(10):
                    card = random.choice(self.deck)
                    player.append(card)
                    self.deck.remove(card)

            elif self.number_of_players == 3:
                for y in range(7):
                    card = random.choice(self.deck)
                    player.append(card)
                    self.deck.remove(card)

            elif self.number_of_players == 4:
                for y in range(6):
                    card = random.choice(self.deck)
                    player.append(card)
                    self.deck.remove(card)
        return player

    def add_points(self, point1 = 0, point2 = 0, point3 = 0, point4 = 0): #Add points to players
        if self.number_of_players == 2:
            self.players_points['Player1'] += point1
            self.players_points['Player2'] += point2

        elif self.number_of_players == 3:
            self.players_points['Player1'] += point1
            self.players_points['Player2'] += point2
            self.players_points['Player3'] += point3

        elif self.number_of_players == 4:
            self.players_points['Player1'] += point1
            self.players_points['Player2'] += point2
            self.players_points['Player3'] += point3
            self.players_points['Player4'] += point4

        return self.players_points

    def i_dont_know(self):
        self.numbers = {'Ace': 11, 'King': 4, 'Queen': 3, 'Jack': 2, '10': 10, '9': 0}
        self.figures = {'Spades': 40, 'Clubs': 60, 'Diamonds': 80, 'Hearts': 100}
        players = [self.players1, self.players2]
        player_points = []
        for x in players:
            points = 0
            for y in x:
                splited_player = y.split(' ')
                points += self.numbers[splited_player[1]]
            player_points.append(points)
        #self.add_points(player_points[0], player_points[1])

        if 'Clubs Queen' in self.players1 and 'Clubs King' in self.players1:
            #self.add_points(self.figures['Clubs'])
            player_points[0] += self.figures['Clubs']

        if 'Diamonds Queen' in self.players1 and 'Diamonds King' in self.players1:
            #self.add_points(self.figures['Diamonds'])
            player_points[0] += self.figures['Diamonds']

        if 'Hearts Queen' in self.players1 and 'Hearts King' in self.players1:
            #self.add_points(self.figures['Hearts'])
            player_points[0] += self.figures['Hearts']

        if 'Spades Queen' in self.players1 and 'Spades King' in self.players1:
            #self.add_points(self.figures['Spades'])
            player_points[0] += self.figures['Spades']

        return player_points

    def auction(self):
        clubs, diamonds, hearts, spades = 0, 0, 0, 0
        players = [self.players1, self.players2]
        players_max_bid = []
        for x in players:
            if 'Clubs Queen' in x and 'Clubs King' in x:
                clubs = 60

            if 'Diamonds Queen' in x and 'Diamonds King' in x:
                diamonds = 80

            if 'Hearts Queen' in x and 'Hearts King' in x:
                hearts = 100

            if 'Spades Queen' in x and 'Spades King' in x:
                spades = 40

            players_max_bid.append(clubs + diamonds + hearts + spades + 120)

        return players_max_bid

    def checking_auction(self, bid_p1, bid_p2):
        bids = [bid_p1, bid_p2]
        for x in bids:
            if x < 100 or x > self.auction()[bids.index(x)]:
                return False
        return True

    #def game(self, card_p1, card_p2):






g1 = Thousend(2)

print(g1.players1)
print(g1.players2)
#print(g1.players3)
#print(g1.players4)
print(len(g1.deck))
print(g1.i_dont_know())
print(g1.players_points)
#print(g1.auction())
print(g1.checking_auction(100,100))