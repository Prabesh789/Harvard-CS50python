import random

# from random import choice
# coin = choice(["heads", "tails"])

coin = random.choice(["heads", "tails"])
print(coin)

#  generate the random number:  random.randint(a, b)

number = random.randint(1, 10)
print(number)

# suffle

cards = ["jack", "king", "queen"]
random.shuffle(cards)
for card in cards:
    print(card)
