name_list=[]
question='y'

while question != 'n':
    def listname():
    while True:
        try:
            Nlist=str(input("Enter Your Name: "))
            continue
        except ValueError:
            print("names dont have numbers")
            continue


        