#!PythonProjects/env python
# Davenport University
# Class Info: CISP253-23151 (Winter 2022)
# Author: Alexander Rogers
# Contact: arogers23@email.davenport.edu

# Program name: simple_hex_bin_converter.py
"""
Example of how a Python programs can use functions and if/elif/else statements to convert input variables into
hexadecimal or binary values.
"""

def again():
    """
        again function acts as a menu that returns the input from the user on what function to run, or to exit the
        program.
            Vars:
                again_input: Records the user input to determine what function to run
            if/elif/else:
                If the variable again_input is set to 1, the again function will call the hex2bin function. However if
                set to 2, then the bin2hex function runs. And finally, if set to N, then the function ends the program.

    """
    again_input = input('''
Hex or Binary Conversion? 1 or 2 (N for End).
''')

    # Run hex2bin function.
    if again_input.upper() == '1':
        hex2bin()
        again()

    # Run bin2hex function.
    elif again_input.upper() == '2':
        bin2hex()
        again()

    # End the program.
    elif again_input.upper() == 'N':
        print('End.')
        exit()
    else:
        again()


def hex2bin():
    """
        hex2bin function converts a hexadecimal value, and converts it to a string of binary numbers including
        leading zeros, hence the while statement which prints out the full conversion values of a hexadecimal value.
            Vars:
                hex_num: Records the user hexadecimal input.
                bin_num: Records the newly converted number into a string.
                hex_len: Records the length of the string
                i: The counter of characters in the string.
            if/elif/else:
                If the variable again_input is set to 1, the again function will call the hex2bin function. However if
                set to 2, then the bin2hex function runs. And finally, if set to N, then the function ends the program.

    """
    print("Enter the Hexadecimal Number: ")
    hex_num = input()
    bin_num = ""
    hex_len = len(hex_num)
    i = 0

    # While loop for characters in the length of the hexadecimal value input.
    while i < hex_len:
        if hex_num[i] == '0':
            bin_num = bin_num + "0000"
        elif hex_num[i] == '1':
            bin_num = bin_num + "0001"
        elif hex_num[i] == '2':
            bin_num = bin_num + "0010"
        elif hex_num[i] == '3':
            bin_num = bin_num + "0011"
        elif hex_num[i] == '4':
            bin_num = bin_num + "0100"
        elif hex_num[i] == '5':
            bin_num = bin_num + "0101"
        elif hex_num[i] == '6':
            bin_num = bin_num + "0110"
        elif hex_num[i] == '7':
            bin_num = bin_num + "0111"
        elif hex_num[i] == '8':
            bin_num = bin_num + "1000"
        elif hex_num[i] == '9':
            bin_num = bin_num + "1001"
        elif hex_num[i] == 'a' or hex_num[i] == 'A':
            bin_num = bin_num + "1010"
        elif hex_num[i] == 'b' or hex_num[i] == 'B':
            bin_num = bin_num + "1011"
        elif hex_num[i] == 'c' or hex_num[i] == 'C':
            bin_num = bin_num + "1100"
        elif hex_num[i] == 'd' or hex_num[i] == 'D':
            bin_num = bin_num + "1101"
        elif hex_num[i] == 'e' or hex_num[i] == 'E':
            bin_num = bin_num + "1110"
        elif hex_num[i] == 'f' or hex_num[i] == 'F':
            bin_num = bin_num + "1111"

        # Add to the i counter.
        i = i + 1

    # Displays the binary value with leading zeros.
    print("\nBinary Value: ", bin_num)


def bin2hex():
    """
        bin2hex function converts a binary value, and converts it to a string of hexadecimal value, hence since
        leading zeros are not as much of a factor in determining the appropriate hex for most applications, it
        can be left out.
            Vars:
                bin_num: Records the user input of a binary string and outputs a hexadecimal number as an integer.
            Note: This can be manually converted as above, for either printing leading hexadecimal values, or string
            interpretations.

    """
    print("Enter a Binary Number:")
    bin_num = input()

    # Convert the binary value input by the user into a hexadecimal value, where hex(int( and the base 2 represent
    # how the number is converted using built in python modules.
    print("\nHex Value: ", hex(int(bin_num, 2)))
    again()

# Hex and Binary conversion selection input for which task is to be performed,
# then paste/type the desired values for conversion.
def main():
    """
        main function returns the menu in which the user can select a desired conversion method, the again function,
        or to exit the program.
            Vars:
                main_input: Records the input by the user to select which conversion method desired.
            Note: This makes the menu more expandable for additional functions, such as inputting 3 for decimal to
            hexadecimal conversions, and so forth.

    """
    main_input = input('''Enter 1 for Hex to Binary, Enter 2 for Binary to Hex (N for End). ''')

    # Run hex2bin function.
    if main_input.upper() == '1':
        hex2bin()
        again()

    # Run bin2hex function.
    elif main_input.upper() == '2':
        bin2hex()
        again()

    # Exit the program.
    elif main_input.upper() == 'N':
        print('End.')
        exit()
    else:
        main()


# Run main function.
main()
