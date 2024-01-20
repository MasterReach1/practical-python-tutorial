class Calculator:
    def __init__(self):
        self.ADDITION_OPERATOR = '+'
        self.SUBTRACT_OPERATOR = '-'
        self.MULTIPLY_OPERATOR = '*'
        self.DIVISION_OPERATOR = '/'
        self.OPERATORS = '+-*/'
    
    def get_user_input_string(self):
        print("Symbols allowed: \n[+ for addition]\n[- for subtraction]\n[* for multiplication]\n[/ for division]")
        user_input_string = input("Enter an equation here >> ")
        return user_input_string.replace(' ', '')

    def get_two_sides_of_equation(self, user_input_string):
        self.index_of_operator = 0
        self.equation_array = []

        for i in range(len(user_input_string)):
            if user_input_string[i] in self.OPERATORS:
                self.index_of_operator = i
                self.equation_array = user_input_string.split(user_input_string[i])
                break
        
        return self.equation_array

    def add_numbers(self, numbers):
        self.sum = 0

        for number in numbers:
            self.sum += int(number)
        return self.sum
    
    def subtract_numbers(self, numbers):
        self.difference = 0
        
        for i in range(len(numbers)):
            if i == 0:
                self.difference = int(numbers[i])
            else: 
                self.difference -= int(numbers[i])
        return self.difference
    
    def multiply_numbers(self, numbers):
        self.product = 1

        for number in numbers:
            self.product *= int(number)
        return self.product
    
    def divide_numbers(self, numbers):
        self.quotient = 0
        
        for i in range(len(numbers)):
            if i == 0:
                self.quotient = int(numbers[i])
            else: 
                self.quotient /= int(numbers[i])
        return self.quotient