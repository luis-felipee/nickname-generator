import random
from adjectives import adjectives
numbers = "0123456789"
symbol = '_'

adjective = random.choice(adjectives)
all =  numbers + symbol
length = 5

rand = "".join(random.sample(all, length))
nickName = adjective + rand
print("The name generate is:", nickName)