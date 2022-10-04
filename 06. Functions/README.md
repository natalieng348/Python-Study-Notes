# Functions

## Function stubs

### Definitions

Function stubs are fuction definitions whose statements haven't been written yet.

Incremental development: a small amount of code is written and tested, then a small amount more (an incremental amount) is written and tested, and so on.

### Benefits of function stubs

* The high-level behavior of the program is captured before diving into details of each function
* Capturing high-level behavior leads to better-organized code, reduced development time, and code with fewer bugs

### Examples

1. Using the _**pass**_ keyword to perform no operation except to act as a placeholder for a required statement.

    ```
    def steps_to_feet(num_steps):
        feet_per_step = 3
        feet = num_steps * feet_per_step
        return feet

    def steps_to_calories(num_steps):
        pass  

    steps = int(input('Enter number of steps walked: '))

    feet = steps_to_feet(steps)
    print('Feet:', feet)

    calories = steps_to_calories(steps)
    print('Calories:', calories)
    ```

2. Printing a message when a function stub is called, alerting the user to the missing function statements. It is good practice to return `-1` for a fuction that will have a return value. 

    ```
    def step_to_calories(steps):
      print('FIXME: finish steps_to_calories')
      return -1
    ```

3. Stop executing if an unfinished fucntion is called using `NotImplementedError`

    ```
    def step_to_calories(steps):
      raise NotImplementedError
      
    """
    Result: 
    Traceback (most recent call last):
    File "<stdin>", line 10, in glt;module<
    File "<stdin>", line 2, in step_to_calories
    NotImplementedError
    """
    ```

## Function arguments

 When a function modifies a parameter, whether or not that modification is seen outside the scope of the function depends on the i of the argument object.
 
 * If immutable (str or int), modification is limited to inside the function.
 * If mutable (list or dict), modification can be seen outside the scope of the function.
 

## Keyword arguments

Keyword arguments that allow arguments to map to parameters by name.

When using keyword arguments, the argument list does not need to follow a specific ordering.

Good practice is to use keyword arguments for any function containing more than approximately 4 arguments.

Examples:

1. Without keyword argument:

```
def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description('The Lord of the Rings', 'J. R. R. Tolkien', 'George Allen & Unwin', 
                       1954, 1.0, 22, 456)
```
 
 2. With keyword argument:
 
 ```
 ef print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description(title='The Lord of the Rings', publisher='George Allen & Unwin',
                       year=1954, author='J. R. R. Tolkien', version=1.0,
                       num_pages=456, num_chapters=22)
 ```

## Default parameter values

When a function call omits an argument, and the default parameter value will be substituted for the corresponding omitted argument

Example:

```
def print_date(day, month, year, style=0):
    if style == 0:  # American
        print(month, '/', day, '/', year)
    elif style == 1:  # European
        print(day, '/', month, '/', year)
    else:
        print('Invalid Style')

print_date(30, 7, 2012, 0)
print_date(30, 7, 2012, 1)
print_date(30, 7, 2012)  # style argument not provided! Default value of 0 used.
```

Common error: providing a mutable object (such as a list) as a default parameter. 
    * Modification of the default parameter object will persist across function calls.
  
Good example:

```
def append_to_list(value, my_list=None):  # Use default parameter value of None
    if my_list == None:  # Create a new list if a list was not provided
        my_list = []
    my_list.append(value)
    return my_list

numbers = append_to_list(50)  # default list appended with 50
print(numbers)
numbers = append_to_list(100)  # default list appended with 100
print(numbers)
```

## Docstrings

A docstring is a string literal placed at the first line of a function body.

We use docstrings to document functions. Good practice is to keep the docstring fof a simple function on a single line.

Example:

```
def print_output():
    """Prints output after calculation"""
    # Function body statements...
```

## The help() function

The help() function prints out the docstring for the function, providing the programmer with information about how to call that function.

