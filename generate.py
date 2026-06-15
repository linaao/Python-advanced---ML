import random
from statistics import mean
import sys

coin = random.choice(["Tails","Heads"])

print(coin)

alph = random.randint(1,1000)

print(alph)


lon = ["cards", "jack", "Queen"]
random.shuffle(lon)

for card in lon:
    print(lon)

averages = mean([100,90])
print(averages)

