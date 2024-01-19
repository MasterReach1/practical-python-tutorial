ADDITION_OPERATOR = '+'
SUBTRACT_OPERATOR = '-'
MULTIPLY_OPERATOR = '*'
DIVISION_OPERATOR = '/'
OPERATORS = '+-*/'

while True:
    print("Symbols allowed: \n[+ for addition]\n[- for subtraction]\n[* for multiplication]\n[/ for division]")
    user_input_string = input("Enter an equation here >> ")

    user_input_string = user_input_string.replace(' ', '')

    index_of_operator = 0
    equation_array = []

    for i in range(len(user_input_string)):
        if user_input_string[i] in OPERATORS:
            index_of_operator = i
            equation_array = user_input_string.split(user_input_string[i])
            break

    if index_of_operator == 0:
        print("Operator not found...")
    else:
        if user_input_string[index_of_operator] == ADDITION_OPERATOR:
            print(int(equation_array[0]) + int(equation_array[1]))
        elif user_input_string[index_of_operator] == SUBTRACT_OPERATOR:
            print(int(equation_array[0]) - int(equation_array[1]))
        elif user_input_string[index_of_operator] == MULTIPLY_OPERATOR:
            print(int(equation_array[0]) * int(equation_array[1]))
        elif user_input_string[index_of_operator] == DIVISION_OPERATOR:
            print(int(equation_array[0]) / int(equation_array[1]))