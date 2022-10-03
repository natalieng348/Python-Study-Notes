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
 
