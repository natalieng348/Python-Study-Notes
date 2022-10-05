"""
6.21 LAB: Convert to Binary
IS 640 - Natalie Nguyen

Write a program that takes in a positive integer as input, 
and outputs a string of 1's and 0's representing the integer in binary. 

The program must define and call the following two functions:
    def int_to_reverse_binary(integer_value)
    def string_reverse(input_string)
"""


# Define your functions here.
def int_to_reverse_binary(integer_value):
    """Takes an integer as a parameter and returns a reverse binary string"""
    result = ""
    while integer_value > 0:
        result += str(integer_value % 2)
        integer_value = integer_value // 2
    return result                           # return result type str

def string_reverse(input_string):
    """Takes an input string as a parameter and returns a reverse of that string"""
    binary_result = ""
    for character in input_string[::-1]:    # reverse str with slicing
        binary_result += character 
    return binary_result                    # return result type str

if __name__ == '__main__':
    """Main function"""
    # Get user input
    user_str = input()
    user_int = int(user_str)
    
    # Call int_to_reverse_binary() to get binary str in a reverse order
    reversed_binary_str = int_to_reverse_binary(user_int)
    
    # Call string_reverse() to get a str representing the input str in reverse
    bin_result = string_reverse(reversed_binary_str)
    
    # Print output
    print(bin_result)