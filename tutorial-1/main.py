number_1 = int(input("Enter a number >> "))

number_2 = int(input("Enter another number >> "))

operation = input("Please say 'add', 'subtract', 'multiply', or 'divide.'")

if (operation == 'add'):
    print(f"The sum is {number_1 + number_2}")
elif (operation == 'subtract'):
    print(f"The difference is { number_1 - number_2 }")
elif (operation == 'multiply'):
    print(f"The product is { number_1 * number_2 }")
elif (operation == 'divide'):
    print(f"The quotient is {number_1 / number_2}")
else:
    print("Invalid input")