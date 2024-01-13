number_1 = int(input("Enter your number here >> "))

number_2 = int(input("Enter your second number here >> "))

operation = input('Enter \'add\', \'subtract\', \'multiply\', or \'divide\' >> ')

if (operation.lower() == 'add'):
    print(number_1 + number_2)
elif (operation.lower() == 'subtract'):
    print(number_1 - number_2)
elif (operation.lower() == 'multiply'):
    print(number_1 * number_2)
elif (operation.lower() == 'divide'):
    print(number_1 / number_2)
else:
    print("Invalid input")