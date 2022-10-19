def main():

    names=[]
    grades=[]
    total = 0
    add_another='y'
    while add_another!='n':
        names.append(input('Enter the name of the student '))
        while True:
            grade=input(f"please enter the letter grade for {names[-1]}").upper()
            if grade in['A','B','C','D','F']:
                grades.append(grade) 
                total = total + convert(grade)
                break
            else:
                print('you did not enter a correct value. \nPlease use the A-F scale.')
        while True:
            add_another = input("would you like to add another\n [Y|n]").lower()
            if add_another in ['y','','n']:
                break
            else:
                print("incorrect entery. Please use a 'y' for yes or 'n' for no.")
    class_size = len(names)
    gpa=round(total/class_size, 1)
    for name, grade in zip(names, grades):
        print(f"{name}: {grade}")
    print(f" The class GPA is {gpa}")
    with open("class_average.txt","w") as file:
        for name,grade in zip(names,grades):
            file.write(f"{name:} {grade}\n")
        file.write(f'Class GPA is {gpa}.')
    return

def convert(grade):
    if grade == 'A':
        return 4
    elif grade == "B":
        return 3
    elif grade =="C":
        return 2
    elif grade == "D":
        return 1
    else:
        return 0 

if __name__=="__main__":
    main()