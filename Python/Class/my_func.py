def get_int():
    while True:
        try:
            x=int(input("enter a number "))
            return x
        except ValueError:
            print("that is no number enter a number ")
            continue