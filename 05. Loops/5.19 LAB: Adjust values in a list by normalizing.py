"""
5.19 LAB: Adjust values in a list by normalizing

When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data.
This adjustment can be done by normalizing to value between 0 and 1, or throwing away outliers.

For this program, adjust the values by dividing all values by the largest value.
The input begins with an integer indicating the number of floating-point values that follow.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

Ex: If the input is:
5
30.0
50.0
10.0
100.0
65.0

the output is:
0.30
0.50
0.10
1.00
0.65

The 5 indicates that there are five floating-point values in the list,
namely 30.0, 50.0, 10.0, 100.0, and 65.0. 100.0 is the largest value in the list, so each value is divided by 100.0.
"""


user_list = []

while True:
    user_input = float(input())       # get user input
    user_list.append(user_input)    # append input to list
    first_value = user_list[0]      # get the first list value
    list_index = user_list.index(user_input)
    if (list_index + 1) > first_value:    # compare new input with the first list value
        break

# pop the first integer in list
user_list.pop(0)

# get the largest number
largest_number = 0
for number in user_list:
    if number > largest_number:
        largest_number = number
    else:
        pass

# divide all list values by the largest value
for number in user_list:
    divided_number = number / largest_number
    print(f'{divided_number:.2f}')
