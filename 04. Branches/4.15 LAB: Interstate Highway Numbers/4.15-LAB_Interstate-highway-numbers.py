# Take user input
highway_number = int(input())

# Global variables
is_primary = 1 <= highway_number <= 99
is_auxiliary = 100 <= highway_number <= 999
is_even = highway_number % 2 == 0

# Check if primary/auxiliary and going EW/NS
if is_primary:
    if is_even:
        print(f'I-{highway_number} is primary, going east/west.')
    else:
        print(f'I-{highway_number} is primary, going north/south.')
elif is_auxiliary:
    last_two_digits = highway_number % 100
    if last_two_digits == 0:
        print(f'{highway_number} is not a valid interstate highway number.')
    else:
        if is_even:
            print(f'I-{highway_number} is auxiliary, serving I-{last_two_digits}, going east/west.')
        else:
            print(f'I-{highway_number} is auxiliary, serving I-{last_two_digits}, going north/south.')
else:
    print(f'{highway_number} is not a valid interstate highway number.')