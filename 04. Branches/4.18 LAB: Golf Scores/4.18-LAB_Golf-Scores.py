"""
4.19 LAB: Golf Scores
"""

# Get user inputs
par_num = int(input())
stroke = int(input())

# Set up global variables
difference = par - stroke   # Diff between par and stroke
par_range = (3, 4, 5)       # Range of par values
eagle = difference == 2
birdie = difference == 1
par = difference == 0
bogey = difference == -1

# Print appropriate score name
if par_num in par_range:
    if eagle:
        print("Eagle")
    elif birdie:
        print("Birdie")
    elif par:
        print("Par")
    elif bogey:
        print("Bogey")
    else:
        print(end='')
else:
    print("Error")
