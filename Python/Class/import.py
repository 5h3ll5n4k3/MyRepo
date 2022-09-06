# import random

# print(random.randint(1,10))

from random import randint as rand


flip = rand(1,2)
if flip == 1:
    print('Tails')
else:
    print("heads")