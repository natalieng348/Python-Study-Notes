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
