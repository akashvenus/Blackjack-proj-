import random
numbers = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack",
"Queen","King","Ace")
suit = ("Spades","Hearts","Clubs","Diamonds")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10
,"King":10,"Ace":(1,11)}

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + "of" + self.suit

class Deck:
    def __init__(self):
        self.full_deck = []
        for s in suit:
            for r in numbers:
                self.full_deck.append(Card(s,r))

    def shuffle(self):
        return random.shuffle(self.full_deck)


    def deal(self,hand1,hand2):
        for _ in range(2):
            hand1.append(self.full_deck.pop())
            hand2.append(self.full_deck.pop())
        return

    def hit(self,hand):
        hand.append(self.full_deck.pop())
        return

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []

    def balance(self,amt):
        print("Your available balance", amt)

    def ace_chooser(self,hand):
        count = 0
        for i in range(len(hand)):
            if "Ace" in hand[i].rank:
                chooser = int(input("Choose 1 or 11 "))
                if chooser == 1:
                    count += hand[i].value[0]

                else:
                    count += hand[i].value[1]

            else:
                count += hand[i].value
        return count


class Dealer:
    def __init__(self):
        self.hand = []

    def balance(self,amt):
        print("Dealer balance", amt)

    def points(self,hand):
        count = 0
        for j in range(len(hand)):
            if "Ace" in hand[j].rank:
                if 0<=count<=10:
                    count += hand[j].value[1]
                elif 11<=count<=20:
                    count += hand[j].value[0]
            else:
                count += hand[j].value
        return count

    def hit_deal(self,hand):
        count = self.points(dealer.hand)
        if 0<=count<=15:
            return "Dealer_hitting"

        elif count > 21:
            return "Busted"

        elif count == 21:
            return "Dealer_got_21"

        else:
            return "Break"


#Game starts
player = Player("Akash")
dealer = Dealer()
print("Welcome the BlackJack ",player.name)
while True: #Balance checker
    balance = int(input("To play you have minimum 10$ "))
    if balance < 10:
        print("You cannot enter the game")
    else:
        False
        break
cond = True
while cond:
    game_on = True
    while game_on: #Round starts
        player.balance(balance)
        deck = Deck()
        deck.shuffle()
        player.hand = []
        dealer.hand = []
        deck.deal(player.hand,dealer.hand)
        not_stay = True
        while not_stay:
            print("Your hand" , *player.hand)
            count1 = player.ace_chooser(player.hand)
            print(count1)
            hit_checker = input("Would you like to hit (Y/N) ").upper()
            if hit_checker == "Y" and count1 <= 21:
                deck.hit(player.hand)

            elif hit_checker == "N" and count1 <=21:
                not_stay = False
                break
            else:
                print("Busted, Dealer wins")
                not_stay = False
                game_on = False
                break
        if game_on == False:
            break
        dealer_amt = 100
        dealer.balance(dealer_amt)
        deal_choice = True
        while deal_choice:
            if dealer.hit_deal(dealer.hand) == "Dealer_hitting":
                deck.hit(dealer.hand)

            if dealer.hit_deal(dealer.hand) == "Busted":
                deal_choice = False
                game_on = False
                print("Dealer Busted, Player wins")
                break
            if dealer.hit_deal(dealer.hand) == "Dealer_got_21":
                deal_choice = False
                break

            if dealer.hit_deal(dealer.hand) == "Break":
                deal_choice = False
                break

        print("Dealer hand" , *dealer.hand)
        count2 = dealer.points(dealer.hand)
        print(count2)
        if game_on == False:
            break
        if count2 > count1:
            print("Dealer wins")
            balance -= 2
            player.balance(balance)
            dealer_amt += 5
            dealer.balance(dealer_amt)
            game_on = False

        elif count2 < count1:
            print("Player wins")
            dealer_amt -= 2
            dealer.balance(dealer_amt)
            balance += 5
            player.balance(balance)
            game_on = False
        else:
            print("Tie round")
            game_on = False

    if balance == 0:
        cond == False
        break     
    again = input("Do you wish to play again (Y/N)").upper()
    while True:
        if again == "Y":
            game_on = True
            break

        elif again == "N":
            cond = False
            break
        else:
            print("Try again")
    if cond == False:
        break
