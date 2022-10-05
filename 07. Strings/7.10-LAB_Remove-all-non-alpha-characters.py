"""
7.10 LAB: Remove all non-alpha characters
IS 640 - Natalie Nguyen

Write a program that removes all non-alpha characters from the given input.

Ex: If the input is:

-Hello, 1 world$!
the output is:

Helloworld
"""

def get_input():
    """Get user input"""
    input_str = input()
    return input_str


def print_output(string):
    """Print result"""
    print(string)


if __name__ == "__main__":
    # Get input
    user_input = get_input()
    
    # check if input contains non-alpha characters
    clean_str = ''
    for character in user_input:
        if character.isalpha() == True:
            clean_str += character
        else:
            continue
    
    # print result
    print_output(clean_str)
