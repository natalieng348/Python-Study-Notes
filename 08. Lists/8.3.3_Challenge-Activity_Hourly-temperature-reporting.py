"""Challenge Activity 8.3.3 - Hourly temperature reporting.

Write a loop to print all elements in hourly_temperature. 
Separate elements with a -> surrounded by spaces.

Sample output for the given program with input: '90 92 94 95'
90 -> 92 -> 94 -> 95 
Note: 95 is followed by a space, then a newline.
"""

user_input = input()
hourly_temperature = user_input.split()

for temp in hourly_temperature:
    if temp != hourly_temperature[-1]:
        print(temp, end = ' -> ')
    else:
        print(temp)