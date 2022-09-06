# import random

# flip =random.randint(1,2)
# if flip ==1:
#     print('heads')
# else:
#     print('Tails')

################################### Different Way

from random import randint as rand


flip = rand(1,2)
if flip == 1:
    print('Tails')
else:
    print("heads")