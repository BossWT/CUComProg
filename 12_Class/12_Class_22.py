class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return "(" + self.value + " " + self.suit + ")"

    def getScore(self):
        if self.value == "A":
            return 1
        elif self.value == "J" or self.value == "Q" or self.value == "K":
            return 10
        else:
            return int(self.value)

    def sum(self, other):
        return (self.getScore() + other.getScore()) % 10

    def __lt__(self, rhs):
        values = ["3", "4", "5", "6", "7", "8",
                  "9", "10", "J", "Q", "K", "A", "2"]
        suits = ["club", "diamond", "heart", "spade"]
        return (values.index(self.value), suits.index(self.suit)) < (values.index(rhs.value), suits.index(rhs.suit))


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n - 1):
    print(Card.sum(cards[i], cards[i + 1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])
