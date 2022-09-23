"""
5.17 LAB: Print string in reverse

Write a program that takes in a line of text as input, and outputs that line of text in reverse.
The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

Ex: If the input is:
"Hello there
Hey
done"

then the output is:
"ereht olleH
yeH"
"""

while True:
    user_input = input()            # get user input
    reversed_output = ''            # output variable
    input_length = len(user_input)  # calculate input length used in for-loop
    end = user_input == "Done" or user_input == "done" or user_input == "d"     # when user wants to end
    if end:
        break
    else:
        for index in range(0, -input_length, -1):
            reversed_output += user_input[index - 1]    # append the last char of input to the output variable
        print(reversed_output)  # print output and loop back to beginning
