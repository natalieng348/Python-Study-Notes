# Define your function here.
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    """Calculates dollar cost to drive given a specific mileage """
    total_gallon = miles_driven / miles_per_gallon
    cost = dollars_per_gallon * total_gallon
    return cost 

if __name__ == '__main__':
    # Get user input
    miles_per_gallon_str = input()
    miles_per_gallon_float = float(miles_per_gallon_str)
    dollars_per_gallon_str = input()
    dollars_per_gallon_float = float(dollars_per_gallon_str)
    
    # Function calls & print output
    your_value = driving_cost(miles_per_gallon_float, dollars_per_gallon_float, miles_driven=10)
    print(f'{your_value:.2f}')
    
    your_value = driving_cost(miles_per_gallon_float, dollars_per_gallon_float, miles_driven=50)
    print(f'{your_value:.2f}')

    your_value = driving_cost(miles_per_gallon_float, dollars_per_gallon_float, miles_driven=400)
    print(f'{your_value:.2f}')