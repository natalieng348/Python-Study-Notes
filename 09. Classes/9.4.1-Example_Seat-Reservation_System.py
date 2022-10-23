"""
Seat Reservation System

Using classes to implement an airline seat reservations system with instance data members and methods.
"""

class Seat:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.paid = 0.0
       
        
    def reserve(self, f_name, l_name, amt_paid):
        self.first_name = f_name
        self.last_name = l_name
        self.paid = amt_paid
    
    
    def make_empty(self):
        self.first_name = ''
        self.last_name = ''
        self.paid = 0.0
    
    
    def is_empty(self):
        return self.first_name == ''
    
    
    def print_seat(self):
        print(f'{self.first_name} {self.last_name}, Paid: {self.paid:.2f}')
        

def make_seats_empty(seats):
    for seat in seats:
        seat.make_empty()
        

def print_seats(seats):
    for index in range(len(seats)):
        print(f'{index}:', end=' ')
        seats[index].print_seat()
        
        
# Set number of available seats
num_seats = 5
available_seats = []

for seat_number in range(1, num_seats+1):
    available_seats.append(Seat())


# print command menu & get user input
print('Command menu:\n'
      + 'p - Print available seats\n'
      + 'r - Reserve a seat\n'
      + 'q - Quit')
command = input('Enter command (p/r/q): ')
print('')

# main function
while command != 'q':
    if command == 'p':      # Print available seats
        print_seats(available_seats)
    elif command == 'r':    # reserve a seat
        seat_num = int(input('Enter seat number (1-5): '))
        if not available_seats[seat_num].is_empty():
            print('Seat not available. Please select another seat.')
        else:
            fname = input('Enter first name: ')
            lname = input('Enter last name: ')
            paid = float(input('Enter amount paid: '))
            print('\n')
            available_seats[seat_num].reserve(fname, lname, paid)
    elif command == 'q':
        print('Quit reservation.')  
        break
    else:
        print('Invalid command. Please select a valid command (p/r/q).')
    
    command = input('Enter command (p/r/q): ')
