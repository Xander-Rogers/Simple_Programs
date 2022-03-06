#!PythonProjects/env python
# Davenport University
# Class Info: CISP253-23151 (Winter 2022)
# Author: Alexander Rogers
# Contact: arogers23@email.davenport.edu

# Program name: simple_calculator.py
"""
Example of how a Python programs can use functions and if/else statements to create a simple calculator.
"""


def addition(var_1, var_2):
    """
            addition function with variable configuration for the first and second input, accounted for as an integer.
                Args:
                    var_1: Set to the first input of the function.
                    var_2: Set to the second input of the function.
                Returns:
                    var_1 in addition to var_2.
                Note:
                    The code written for the operation of addition.
    """
    # Performs addition operation.
    return var_1 + var_2


def subtraction(var_1, var_2):
    """
            subtraction function with variable configuration for the first and second input, accounted for as an
            integer.
                Args:
                    var_1: Set to the first input of the function.
                    var_2: Set to the second input of the function.
                Returns:
                    var_1 subtracted to var_2.
                Note:
                    The code written for the operation of subtraction.
    """
    # Performs subtraction operation.
    return var_1 - var_2


def multiplication(var_1, var_2):
    """
            multiplication function with variable configuration for the first and second input, accounted for as an
            integer.
                Args:
                    var_1: Set to the first input of the function.
                    var_2: Set to the second input of the function.
                Returns:
                    var_1 multiplied to var_2.
                Note:
                    The code written for the operation of multiplication.
    """
    # Performs multiplication operation.
    return var_1 * var_2


def division(var_1, var_2):
    """
            division function with variable configuration for the first and second input, accounted for as an
            integer.
                Args:
                    var_1: Set to the first input of the function.
                    var_2: Set to the second input of the function.
                Returns:
                    var_1 divided by var_2.
                Note:
                    The code written for the operation of division.
    """
    # Performs division operation.
    return var_1 / var_2


def again():
    """
            again function returns the main function called calc, which will run the Simple Calculator again.
                Vars:
                    calc_again as the input by the user.
                if/elif/else statements:
                    Returns:
                           The input of the user to redirect them to either the main function calc, or quit the game.
    """
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')
    # Returns output based on user input.
    if calc_again.upper() == 'Y':
        calc()
        again()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()


def welcome():
    """
            welcome function returns a simple print statement as the "Welcome Page."
    """
    print('''
Welcome to Simple Calculator!
''')


welcome()


def calc():
    """
            calc function returns the main logic of the program runs the operations of the Simple Calculator.
                Vars:
                    choice: The operation selected by the user.
                    var_1:  The first input by the user.
                    var_2:  The second input by the user.
                if/elif/else statements:
                    Returns:
                            The result of var_1 and var_2 respective to the operation selected by the user.
    """
    # Generates the user's initial choice of operation to perform in the calculator.
    choice: int = int(input("Choose an operation: \n"
                            "-> "
                            "1 = Addition "
                            "2 = Subtraction "
                            "3 = Multiplication "
                            "4 = Division: "))

    # Takes var_1 and var_2 input for desired operation.
    var_1 = int(input("Input #1: "))
    var_2 = int(input("Input #2: "))

    # Performs addition operation.
    if choice == 1:
        print(var_1, "+", var_2, "=",
              addition(var_1, var_2))

    # Performs subtraction operation.
    elif choice == 2:
        print(var_1, "-", var_2, "=",
              subtraction(var_1, var_2))

    # Performs multiplication operation.
    elif choice == 3:
        print(var_1, "*", var_2, "=",
              multiplication(var_1, var_2))

    # Performs subtraction operation.
    elif choice == 4:
        print(var_1, "/", var_2, "=",
              division(var_1, var_2))

    # Input is not a number or recognized.
    else:
        print("Invalid input")


# Call functions.
calc()
again()
