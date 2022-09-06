

answer=(input('How would you like to convert:\n  Convert to Celsius(1):\n Convert to Fahrenheit(2) '))

if answer=="1":
        numf=float(input('Enter the temperature in Fahrenheit you would like to convert to Celsius: '))
        numc= (numf - 32) * 5/9
        print(str(numf) + ' Faherenheit converted to celsius is '+ str(round(numc, 1)))

elif answer=="2":
        numc=float(input('Enter the temperature in Celsius you would like to convert to Fahrenheit: '))
        numf= (numc*9/5)+32
        print(str(numc) + ' Celsius converted to Fahrenheit is '+ str(round(numf, 1)))
else:
        print('use the program right dummy')

