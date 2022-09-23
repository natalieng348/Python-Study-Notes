"""
5.15 LAB: Password Modifier

Many user-created passwords are simple and easy to guess.
Write a program that takes a simple password and makes it stronger
by replacing characters using the key below,
and by appending "!" to the end of the input string.

"i" becomes 1
"a" becomes @
"m" becomes M
"B" becomes 8
"s" becomes $
"""

# TODO 1: GET USER INPUT
word = input()
password = ''

# TODO 2: CHECK EACH ELEMENT IN THE USER INPUT USING FOR LOOP & IF-ELIF-ELSE
for character in word:
    if character == 'i':            # "i" becomes 1
        password += '1'
    elif character == 'a':          # "a" becomes @
        password += '@'
    elif character == 'm':          # "m" becomes M
        password += 'M'
    elif character == 'B':          # "B" becomes 8
        password += '8'
    elif character == 's':          # "s" becomes $
        password += '$'
    else:
        password += character

# TODO 4: APPEND "!" TO THE END OF THE STRING
password += "!"

# TODO 5: PRINT UPDATED PASSWORD
print(password)
