# CHAPTER 9: CLASSES

## Instance Methods

* A function defined within a class is known as an instance method.
* An instance method can be referenced using dot notation. 
* __init__ is a special method name -- used for initialization of new instances
  * Good practice is to avoid using the double underscores __ in identifiers to prevent collisions with special method names
* A common error for new programmers is to omit the self argument as the first parameter of a method.

Example:

```
class Employee:
    def __init__(self):         # initializes new instances
        self.wage = 0
        self.hours_worked = 0

    def calculate_pay(self):    # don't forget the 'self' parameter
        return self.wage * self.hours_worked

alice = Employee()
alice.wage = 9.25
alice.hours_worked = 35
print(f'Alice:\n Net pay: {alice.calculate_pay():.2f}')

barbara = Employee()
barbara.wage = 11.50
barbara.hours_worked = 20
print(f'Barbara:\n Net pay: {barbara.calculate_pay():.2f}')
```

## Class and Instance Object Types

* Class attributes are assignments within the class definition
  * Example: `area_code` is a class attribute
    ```
    class PhoneNumber:
       area_code = '805'
       def __init__(self):
           self.number = '555-1234'
    ```
 <br>
 
 * Instance attributes are instance variables that are assigned using dot notation. An instance attribute can be created/changed from outside or inside the function scope
   * Example: `number` is an instance attribute
      ```
      class PhoneNumber:
         def __init__(self):
            self.number = '805-555-1234'
      ```
      
      and
      
      ```
      class PhoneNumber:
         def __init__(self):
            self.number = None
      
      garrett = PhoneNumber()
      garrett.number = '805-555-1234'   # number can be changed outside of the function scope
      ```
   
