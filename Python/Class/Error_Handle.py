# X = int(input("Give me that number!!!\n"))
# print(X)

while True:
    try:
        x=int(input("give me that number: "))
        break
    except ValueError:
        print("you did not give me that number")
        continue

print(x)
