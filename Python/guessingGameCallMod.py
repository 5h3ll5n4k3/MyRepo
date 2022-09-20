from random import randint

def guess():
    while True:
        try:
            x = int(input("Guess a number between 1 and 100: "))
            if x > 101:
                print("You picked a number greater then 100")
                continue
            elif x < 0:
                print("You picked a number less then 0")
                continue
            break
        except ValueError:
            print("You did not enter a number")
            continue
    return x

def main():
    number = randint(1,100)
    counter = 0
    while counter < 5:
        my_guess = guess()
        if my_guess < number:
            print("Your guess is to low.")
            counter += 1
        elif my_guess > number:
            print("Your number is to high")
            counter += 1
        elif my_guess == number:
            print("You win!")
            counter += 10
    
if __name__ == "__main__":
    main()

