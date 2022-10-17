"""
8.19 LAB: Contact list
Natalie Nguyen - IS 640

Write a program that first takes in word pairs that consist of a name and 
a phone number (both strings), separated by a comma. 

That list is followed by a name, and your program should output 
the phone number associated with that name. 
Assume the search name is always in the list.

Ex: If the input is:

Joe,123-5432 Linda,983-4123 Frank,867-5309
Frank

the output is:

867-
"""

# get pairs of names and phone numbers and target name
user_input = input()
target_name = input()
entries = user_input.split()
contacts = {}

# convert user input to dict
for pair in entries:
    split_pair = pair.split(',')
    contacts[split_pair[0]] = split_pair[1]

# Output the number associated with target name
for name, phone_no in contacts.items():
    if name == target_name:
        print(phone_no)