"""
7.8 LAB: Mad Lib - loops
IS 640 - Natalie Nguyen

Write a program that takes a string and an integer as input, 
and outputs a sentence using the input values as shown in the example below. 

The program repeats until the input string is quit 
and disregards the integer input that follows.
"""

def split_input(user_input):
    """Splits input and get input string & integer"""
    split_str = user_input.split()
    user_str = split_str[0]
    user_int = int(split_str[-1])
    return user_str, user_int


def print_output(user_str, user_int):
    """Prints output if input does not contain 'quit'"""
    print(f'Eating {user_int} {user_str} a day keeps the doctor away.')


if __name__ == "__main__":
    """Loops the input to print in a sentence until input contains 'quit'"""
    while True:
        # get user input
        input_str = input()
        
        # assign variables to str and int
        string, integer = split_input(input_str)
        
        # check if str is 'quit'
        if string == 'quit':
            break
        else:
            print_output(string, integer)
