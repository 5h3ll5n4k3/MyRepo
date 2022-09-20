def clear():
    os.system('cls' if os.name== 'nt' else'clear')
    
def get_num(question):
    while True:
        try:
            x =int(input(question))
            return x
        except ValueError:
            print('that is not a number')
            continue
dogs= get_num('how many dogs do you have: ')
print(dogs)