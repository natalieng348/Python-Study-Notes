"""12.13 LAB: Thesaurus
Given a set of text files containing synonyms for different words, 
complete the main program to output the synonyms for a specific word. 

Each text file contains synonyms for the word specified in the file's name, 
and each row within the file lists the word's synonyms that begin with the same letter, separated by a space. 

The program reads a word and a letter from the user and opens the text file associated with the input word. 
The program then stores the contents of the text file into a dictionary predefined in the program. 

Finally the program searches the dictionary and outputs all the synonyms that begin with the input letter,
one synonym per line, or a message if no synonyms that begin with the input letter are found.

Hints: Use the first letter of a synonym as the key when storing the synonym into the dictionary. 
Assume all letters are in lowercase.

Ex: If the input of the program is:

"educate
c"

the program opens the file educate.txt, which contains:

brainwash brief
civilize coach cultivate
develop discipline drill
edify enlighten exercise explain
foster
improve indoctrinate inform instruct
mature
nurture
rear
school
train tutor

then the program outputs:

civilize
coach
cultivate

Ex: If the input of the program is:

educate
a

then the program outputs:

No synonyms for educate begin with a.
"""
# Define dictionary
synonyms = {}

# take user inputs
file_name = input()
first_letter_input = input()

# open and read a csv file
with open(f"{file_name}.txt", mode='r', newline='\n') as f:
    content = f.read()
    
    # replace end line "\n" with ","
    content = content.replace("\n", ",")
    
    # store file data into a list
    synonym_list = content.split(",")
    synonym_list.remove('')
    
    # create a list of first letters of each synonym 
    first_letter_list = [item[0] for item in synonym_list]
    
    # store synonym into the dictionary using the first letter as a key
    for index in range(len(first_letter_list)):
        synonyms[first_letter_list[index]] = synonym_list[index]
    
    # check if the synonym dictionary contains the first letter input 
    if first_letter_input in first_letter_list:
        words = synonyms[first_letter_input].split(' ')
        for word in words:
            print(word)
    else:
        print(f'No synonyms for educate begin with {first_letter_input}.')