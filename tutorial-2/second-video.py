# The all-caps convention of these variables make them constants to
#   anyone who can read in Python. Constants are variables that never
#   need to change. Unlike other languages, constants are NOT defined
#   in Python, hence the need for a convention.
# Always place them at the top of a file or in a constants.py for
#   best practice.

ADDITION_OPERATOR = '+'
SUBTRACT_OPERATOR = '-'
MULTIPLY_OPERATOR = '*'
DIVISION_OPERATOR = '/'
OPERATORS = '+-*/'
NUMBERS = "1234567890"

# This is an infinite loop. Never, ever do this in production code. This is done
#   for simplicity's sake in this tutorial, and many beginners often use these
#   in their early days of learning any coding language.
# If you need to exit the application, you have to press Ctrl+C to break the
#   execution.

while True:
    print("Symbols allowed: \n[+ for addition]\n[- for subtraction]\n[* for multiplication]\n[/ for division]")
    user_input_string = input("Enter an equation here >> ")

    # This simple one-liner removes all whitespace from the input string.
    user_input_string = user_input_string.replace(" ", "")

    # The remaining code works because strings are equivalent to arrays in Python.
    # We can treat them as such, iterating them and finding characters
    #   by their indexes. Keep this in mind as you read this code.
    index_of_operator = 0
    equation_array = []

    # Find the index of the operator in the string.
    for i in range(len(user_input_string)):
        if user_input_string[i] in OPERATORS:
            index_of_operator = i
            equation_array = user_input_string.split(user_input_string[i])
            break
    
    # This first check ensures that the loop above actually found an operator
    #   in user_input_string. If the loop does find this, the value of
    #   index_of_operator will be something besides 0.
    
    if index_of_operator == 0:
        print("Operator not found.")
        continue
    else:
        if user_input_string[index_of_operator] == ADDITION_OPERATOR:
            print(int(equation_array[0]) + int(equation_array[1]))
        elif user_input_string[index_of_operator] == SUBTRACT_OPERATOR:
            print(int(equation_array[0]) - int(equation_array[1]))
        elif user_input_string[index_of_operator] == MULTIPLY_OPERATOR:
            print(int(equation_array[0]) * int(equation_array[1]))
        elif user_input_string[index_of_operator] == DIVISION_OPERATOR:
            print(int(equation_array[0]) - int(equation_array[1]))