"""
Challenge Activity 8.5.1: Print multiplication table
Print the two-dimensional list mult_table by row and column. On each line, each character is separated by a space. Hint: Use nested loops.

Sample output with input: '1 2 3,2 4 6,3 6 9':
1 | 2 | 3
2 | 4 | 6
3 | 6 | 9
"""

user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]

''' Your solution goes here '''
for row in mult_table:
    for num in row:
        if num != row[-1]:
            print(num, end=" | ")
        else:
            print(num)
