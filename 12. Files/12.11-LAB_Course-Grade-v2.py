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
midterm1 = []
midterm2 = []
final = []
total_midterm1 = 0
total_midterm2 = 0
total_final = 0
student_id = 1


# TODO: Read a file name from the user and read the tsv file here. 
file_name = input()

with open(file_name, 'r') as tsvfile:
    grades_reader = csv.reader(tsvfile, delimiter='\t')

    for row in grades_reader:
        # Convert score strings to float
        scores = [float(cell) for cell in row[2:]]

    # TODO: Compute student grades and exam averages, then output results to a text file here. 
        # Calculate avg scores for each student
        total_scores = 0
        for score in scores:
            total_scores += score
        avg_score = total_scores / len(scores)
        
        # convert score to letter grade
        if avg_score >= 90:
            letter_grade = 'A'
        elif avg_score >= 80: 
            letter_grade = 'B'
        elif avg_score >= 70: 
            letter_grade = 'C'
        elif avg_score >= 60: 
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        
        # Add letter grade to each row
        row.append(letter_grade)
        
        # Store data in grades dictionary
        grades[student_id] = row
        student_id += 1
    
        # Create lists of grades for each exam
        midterm1.append(float(row[2]))
        midterm2.append(float(row[3]))
        final.append(float(row[4]))
    
    # Calculate midterm1 average
    for m1_grade in midterm1:
        total_midterm1 += m1_grade
    avg_midterm1 = total_midterm1 / len(midterm1)
    
    # Calculate midterm2 average
    for m2_grade in midterm2:
        total_midterm2 += m2_grade
    avg_midterm2 = total_midterm2 / len(midterm2)
    
    # Calculate final average
    for final_grade in final:
        total_final += final_grade
    avg_final = total_final / len(final)
    
with open('report.txt', 'w') as txtfile:
    for value in grades.values():
        for item in value:
            if item == value[-1]:
                txtfile.write(f'{item}\n')
            else:
                txtfile.write(f'{item}\t')
    txtfile.write('\n')            
    txtfile.write(f'Averages: midterm1 {avg_midterm1:.2f}, midterm2 {avg_midterm2:.2f}, final {avg_final:.2f}\n')
    txtfile.close()
    
"""
1: Compare output
Input: StudentInfo.tsv

Your file content:
Barrett	Edan	70	45	59	F
Bradshaw	Reagan	96	97	88	A
Charlton	Caius	73	94	80	B
Mayo	Tyrese	88	61	36	D
Stern	Brenda	90	86	45	C

Averages: midterm1 83.40, midterm2 76.60, final 61.60


2:Compare output
Input: StudentInfo1.tsv
Your file content:
Barber	Ryley	97	65	55	C
Barrett	Edan	98	63	53	C
Bradshaw	Reagan	89	55	38	D
Cabot	Henry	94	97	85	A
Charlton	Caius	41	73	75	D
Flynn	Jane	99	95	70	B
Holder	Guto	59	71	61	D
King	Sonya	85	43	56	D
Mayo	Tyrese	76	57	96	C
Min	Johnny	46	43	67	F
Preston	Mcauley	89	98	94	A
Robison	Lynda	96	90	55	B
Stern	Brenda	68	84	52	D
Stott	Peyton	80	57	59	D
Warner	Gwion	65	36	47	F

Averages: midterm1 78.80, midterm2 68.47, final 64.20

3:Compare output
Input: StudentInfo2.tsv
Your file content: 
Stott	Peyton	80	57	75	C

Averages: midterm1 80.00, midterm2 57.00, final 75.00
"""