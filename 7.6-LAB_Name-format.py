"""
7.6 LAB: Name format
IS 640 - Natalie Nguyen

Write a program whose input is: firstName middleName lastName

and whose output is: lastName, firstInitial.middleInitial.

If the input has the form: firstName lastName

the output is: lastName, firstInitial.
"""

def split_name(name):
    name_split = name.split()
    return name_split


def get_initials_and_lastname(name_split):
    """Splits full name; get first initial, middle initial and last name"""
    f_initial = name_split[0][0]
    m_initial = name_split[1][0]
    l_name = name_split[-1]
    return f_initial, m_initial, l_name


if __name__ == "__main__":
    # Get user input
    full_name = input()
    full_name_split = split_name(full_name)
    
    # Get first initial, middle initial and last name
    first_initial, middle_initial, last_name = get_initials_and_lastname(full_name_split)
    
    # Check if full name contains middle name
    full_name_length = len(full_name_split)
    includes_middle_name = full_name_length == 3
    if includes_middle_name:
        middle_initial = full_name_split[1][0]
        print(f'{last_name}, {first_initial}.{middle_initial}.')
    else:
        print(f'{last_name}, {first_initial}.')