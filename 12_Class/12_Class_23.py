class Card:
    values = ["3", "4", "5", "6", "7", "8",
              "9", "10", "J", "Q", "K", "A", "2"]
    suits = ["club", "diamond", "heart", "spade"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "(" + self.value + " " + self.suit + ")"

    def next1(self):
        suitindex = Card.suits.index(self.suit)
        if self.value == "2" and self.suit == "spade":
            return Card("3", "club")
        elif suitindex < len(Card.suits) - 1:
            suitindex += 1
            return Card(self.value, Card.suits[suitindex])
        else:
            valueindex = Card.values.index(self.value)
            valueindex += 1
            return Card(Card.values[valueindex], Card.suits[0])

    def next2(self):
        suitindex = Card.suits.index(self.suit)
        if self.value == "2" and self.suit == "spade":
            self.value = "3"
            self.suit = "club"
        elif suitindex < len(Card.suits) - 1:
            suitindex += 1
            self.suit = Card.suits[suitindex]
        else:
            valueindex = Card.values.index(self.value)
            valueindex += 1
            self.value = Card.values[valueindex]
            self.suit = Card.suits[0]


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
