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

    def pc_card(self, card_p1): #Computer choose a card to play:
        self.numbers = {'Ace': 11, 'King': 4, 'Queen': 3, 'Jack': 2, '10': 10, '9': 0}
        self.figures = {'Spades': 40, 'Clubs': 60, 'Diamonds': 80, 'Hearts': 100}
        card = card_p1.split(' ')
        playable_cards_pc = {}

        for x in self.players2: #checking which the player can play card
            if card[0] in x:
                playable_cards_pc[x] = self.numbers[x.split(' ')[1]]

        for x in playable_cards_pc: #Searchs the bigger card than player1
            if playable_cards_pc[x] > self.numbers[card[1]]:
                return x

        if len(playable_cards_pc) == 0: #Searchs the lowest card than player1
            player2_cards = {}
            for x in self.players2:
                player2_cards[x] = self.numbers[x.split(' ')[1]]
            return min(player2_cards)
        else:
            return min(playable_cards_pc)

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

    def checking_auction(self, bid_p1, bid_p2=100): #checking if the player has entered the correct number
        bids = [bid_p1, bid_p2]
        for x in bids:
            if x < 100 or x > self.auction()[bids.index(x)]:
                return False
        return True

