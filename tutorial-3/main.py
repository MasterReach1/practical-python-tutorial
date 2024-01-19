from calculator import Calculator

calc = Calculator()

user_input = calc.get_user_input_string()

numbers_array = calc.get_two_sides_of_equation(user_input_string=user_input)

print(calc.divide_numbers(numbers=numbers_array))