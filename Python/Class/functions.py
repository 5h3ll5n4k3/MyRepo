def my_func():
    while True:
        try:
            x = int(input("gimme number: "))
            break
        except ValueError:
            print("that not be a number")
            continue
    return x
num1=my_func()
print(num1)