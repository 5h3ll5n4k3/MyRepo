# import random

# flip =random.randint(1,2)
# if flip ==1:
#     print('heads')
# else:
#     print('Tails')

################################### Different Way

# from random import randint as rand


# flip = rand(1,2)
# if flip == 1:
#     print('Tails')
# else:
#     print("heads")





from random import randint as rand
number = rand(1,100)
print(number)
while True:
    try:
        x=int(input("Guess a number 1-100 \n"))
        if number != x:
            print("Answer was wrong try again you have 3 total tries")
            break    
    except ValueError:
        print("That was not a number")    
       




if  number == x: 
   print("Congratulations that is correct")