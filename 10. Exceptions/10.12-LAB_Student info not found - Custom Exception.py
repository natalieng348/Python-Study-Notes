"""
10.12 LAB: Student info not found - custom exception types
Natalie Nguyen - IS 640

1. Given a main program that searches for the ID or the name of a student from a dictionary,
complete the find_ID() and the find_name() functions that return the corresponding information of a student.

2. Then, insert a try/except statement in main() to catch any exceptions thrown by find_ID() or find_name(), 
and output the exception message. Each entry of the dictionary contains the name (key) and the ID (value) of a student.

3. Function find_ID() takes two parameters, a student's name and a dictionary. 
Function find_ID() returns the ID associated with the student's name if the name is in the dictionary.
Otherwise, the function throws a custom exception type, StudentInfoError, with the message 
"Student ID not found for studentName", where studentName is the name of the student.

4. Function find_name() takes two parameters, a student's ID and a dictionary. 
Function find_name() returns the name associated with the student's ID if the ID is in the dictionary.
Otherwise, the function throws a custom exception type, StudentInfoError, with the message 
"Student name not found for studentID", where studentID is the ID of the student.

5. The main program takes two inputs from a user: a user choice of finding the ID or 
the name of a student (int), and the ID or the name of a student (string).
If the user choice is 0, find_ID() is invoked with the student's name as one of the arguments.
If the user choice is 1, find_name() is invoked with the student's ID as one of the arguments.
The main program finally outputs the result of the search or a message if an exception is caught.

Note:   StudentInfoError is defined in the program as a custom exception type. 
        StudentInfoError has an attribute to store an exception message.
"""

# Define custom exception
class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message  # Initialize the exception message


def find_ID(name, info):
    # Type your code here.
    if name in info.keys():
        return info[name]
    else:
        raise StudentInfoError(f'Student ID not found for {name}')
        
    
def find_name(ID, info):
    # Type your code here.
    if ID in info.values():
       for student_name, student_ID in info.items():
           if ID == student_ID:
               return student_name
    else:
        raise StudentInfoError(f'Student name not found for {ID}')

if __name__ == '__main__':
    # Dictionary of student names and IDs
    student_info = {
        'Reagan' : 'rebradshaw835',
        'Ryley' : 'rbarber894',
        'Peyton' : 'pstott885',
        'Tyrese' : 'tmayo945',
        'Caius' : 'ccharlton329'
    }
    
    userChoice = input()    # Read search option from user. 0: find_ID(), 1: find_name()
    
    # FIXME: find_ID() and find_name() may throw an Exception.
    #        Insert a try/except statement to catch the exception and output any exception message.
    
    if userChoice == "0":
        name = input()
        try:
            result = find_ID(name, student_info)
            print(result)
        except StudentInfoError as message:
            print(message)
    else:
        ID = input()
        try:
            result = find_name(ID, student_info)
            print(result)
        except StudentInfoError as message:
            print(message)
    