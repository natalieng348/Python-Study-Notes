"""
12.11 LAB: Course Grade
Natalie Nguyen - IS 640

Write a program that reads the student information from a tab separated values (tsv) file. 
The program then creates a text file that records the course grades of the students. 

Each row of the tsv file contains the Last Name, First Name, Midterm1 score, Midterm2 score, and the Final score of a student. 
A sample of the student information is provided in StudentInfo.tsv. 

Assume the number of students is at least 1 and at most 20. 
Assume also the last names and first names do not contain whitespaces.

The program performs the following tasks:

- Read the file name of the tsv file from the user.
- Open the tsv file and read the student information.
- Compute the average exam score of each student.
- Assign a letter grade to each student based on the average exam score in the following scale:
    A: 90 =< x
    B: 80 =< x < 90
    C: 70 =< x < 80
    D: 60 =< x < 70
    F: x < 60
- Compute the average of each exam.
- Output the last names, first names, exam scores, and letter grades of the students into a text file named report.txt. 
- Output one student per row and separate the values with a tab character.
- Output the average of each exam, with two digits after the decimal point, at the end of report.txt. 

Hint: Use the format specification to set the precision of the output.
"""
import csv

# TODO: Declare any necessary variables here. 
grades = {}
num_exams = 3
total_midterm1 = 0
total_midterm2 = 0
total_final = 0
      
# TODO: Read a file name from the user and read the tsv file here. 
file_name = input()

with open(file_name, 'r') as tsvfile:
    file_reader = csv.reader(tsvfile, delimiter='\t')
    
    # store course grade data in a dictionary
    student_id = 0
    for line in file_reader:
        grades[student_id] = line
        student_id += 1

     

# TODO: Compute student grades and exam averages, then output results to a text file here. 
 
# Calulate each student average grade
for student_info in grades.values():
    total_grade = int(student_info[2]) + int(student_info[3]) + int(student_info[4])
    avg_grade = total_grade / num_exams
    
    # Convert avg_grade to letter_grade
    if avg_grade >= 90:
        letter_grade = 'A'
    elif avg_grade >= 80: 
        letter_grade = 'B'
    elif avg_grade >= 70: 
        letter_grade = 'C'
    elif avg_grade >= 60: 
        letter_grade = 'D'
    else:
        letter_grade = 'F'
        
    # Add letter grade to each student profile
    student_info.append(letter_grade)


# get total scores for each exam
for student_id in grades.keys():
    total_midterm1 += int(grades[student_id][2])
    total_midterm2 += int(grades[student_id][3])
    total_final += int(grades[student_id][4])
    
# Calculate average scores for each exam
num_students = len(grades)
avg_midterm1 = total_midterm1 / num_students
avg_midterm2 = total_midterm2 / num_students
avg_final = total_final / num_students

print(f'{avg_midterm1:.2f}')
print(f'{avg_midterm2:.2f}')
print(f'{avg_final:.2f}')