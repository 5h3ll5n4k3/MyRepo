from random import *
counter = 0

def question1():
    global counter
    while True:
        try:
            print("Are you a human\n")
            answer1= str(input("A: No\n" "B: Maybe\n" "C: I am an alien\n" "D: Yes\n"))
            if answer1.lower()=='d':
                counter += 1
            break
        except ValueError:
            print("invalid input")
            continue
    return answer1
question1()

def question2():
    global counter
    while True:
            try:
                print("What color is the Sky\n")
                answer2= str(input("A: Blue\n" "B: purple\n" "C: 18\n" "D: lmnop\n"))
                if answer2.lower()=='a':
                    counter += 1
                break
            except ValueError:
                print("invalid input")
                continue
    return answer2
question2()

def question3():
    global counter
    while True:
            try:
                print("What color is the sun\n")
                answer3= str(input("A: Red\n" "B: Orange\n" "C: Plasma\n" "D: The light spectrum has many color waves\n"))
                if answer3.lower()=='d':
                    counter += 1
                break
            except ValueError:
                print("invalid input")
                continue
    return answer3
question3()

def question4():
    global counter
    while True:
            try:
                print("Whats 9+10\n")
                answer4= str(input("A: 12\n" "B: 21\n" "C: 19\n" "D: 88\n"))
                if answer4.lower()=='c':
                    counter += 1
                break
            except ValueError:
                print("invalid input")
                continue
    return answer4
question4()

def question5():
    global counter
    while True:
            try:
                print("Was this the Best Test ever\n")
                answer5= str(input("A: Heck no\n" "B: Absolutly\n" "C: poop quiz\n" "D: mid\n"))
                if answer5.lower()=='b':
                    counter += 1
                break
            except ValueError:
                print("invalid input")
                continue
    return answer5
question5()
def grade():
    if counter==5: 
        print("you get an A")
    elif counter==4:
        print("you get a B")
    elif counter==3:
        print('you get a C')
    elif counter==2:
        print("you get a D")
    elif counter== 1:
        print("you get a F")
    else:
        print('you failed so bad you dont get a score')
grade()


