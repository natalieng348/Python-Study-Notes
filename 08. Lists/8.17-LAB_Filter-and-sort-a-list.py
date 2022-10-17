"""
8.17 LAB: Filter and sort a list

Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).

Ex: If the input is:
10 -7 4 39 -6 12 2

the output is:
2 4 10 12 39 

For coding simplicity, follow every output value by a space. Do not end with newline.
"""

# get user input (str)
user_str = input()

# convert user input into a list of integers
user_list_str = user_str.split()
user_list_int = [int(item) for item in user_list_str]


# loop in list to filter non-neg ints and sort list
for num in user_list_int[:]:    # make a copy of user_list_int to avoid logic error
    if num < 0:
        user_list_int.remove(num)

# sort list
user_list_int.sort()

# print ouput as a str
for num in user_list_int:
    print(num, end=' ')
