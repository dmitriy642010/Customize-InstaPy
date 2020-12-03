import random

names = ['first', 'second', 'third', 'and_others']

print(random.sample(set(names), int(input('How many names to pick?\n'))))
