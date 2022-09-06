my_list = []
question = 'y'
while question != 'n':
    my_list.append(input("give me an item name:\nl"))
    while True:
        question = input('would you like to add another?\n[Y|n]: ')
        if question in ['Y','n','']:
            break
        else:
            print("input error: Please use 'y' or 'n'.")
print(my_list)
