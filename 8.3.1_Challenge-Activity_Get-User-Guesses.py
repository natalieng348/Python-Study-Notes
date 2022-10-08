"""Challenge Activity 8.3.1 - Get User Guesses
IS 640 - Natalie Nguyen

Write a loop to populate the list user_guesses with a number of guesses. 
The variable num_guesses is the number of guesses the user will have, 
which is read first as an integer. 
Read each guess (an integer) one at a time using int(input()).

Sample output with input:
3
9
5
2
user_guesses: [9, 5, 2]
"""


while True:
    num_guesses = int(input())
    user_guesses = []

    if num_guesses <= 0:
    # when user inputs number of guesses <= 0
        print('You entered an invalid input. Try again with a positive integer.')
        continue
    else:
        while True:
            # get user input
            guess = int(input())
            
            # append to user_guesses
            user_guesses.append(guess)
            
            # count length of user_guesses
            cnt_guesses = len(user_guesses)
            
            # check if length of user_guesses < num_guesses
            if cnt_guesses < num_guesses:
                continue
            else:
                break
        print('user_guesses:', user_guesses)