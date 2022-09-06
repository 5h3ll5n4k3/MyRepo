while True:
    try:
        numF=float(input('Enter the temperature in Fahrenheit you would like to convert: '))
        break
    except ValueError:
        print("That is not a number")
        continue
numC= (numF - 32) * 5/9

print(str(numF) + ' Faherenheit converted to celsius is '+ str(round(numC, 2)))