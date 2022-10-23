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

## Class customization

* Class customization is the process of defining how a class should behave for some common operations. 
* Such operations might include printing, accessing attributes, or how instances of that class are compared to each other.
* To cusomize a class, a programmer implements instances methods with *special method names*
* Example: `__str__()` method is used to change how a class instance object is printed
 * Normal printing 
  ```
  class Toy:
     def __init__(self, name, price, min_age):
         self.name = name
         self.price = price
         self.min_age = min_age
     
 truck = Toy('Monster Truck XX', 14.99, 5)
 print(truck)
  ```
  Result: `<__main__.Toy instance at 0xb74cb98c>`
  
 * Customized printing
  ```
  class Toy:
      def __init__(self, name, price, min_age):
         self.name = name
         self.price = price
         self.min_age = min_age
     
      def __str__(self):
         return (f'{self.name} costs only ${self.price:.2f}.'
                 f' Not for children under {self.min_age}!'}
  truck = Toy('Monster Truck XX', 14.99, 5)
  print(truck)
  ```
  Result: `Monster Truck XX costs only $14.99. Not for children under 5!`
  

### Operator Overloading

* Class operators can redefine the functionality of built-in operators like <,>=,+,-,* when used in class instances. This technique is called Operator Overloading

* Rich comparison methods:
 
  | Rich comparison method |      Overloaded operator      |
  |:----------------------:|:-----------------------------:|
  | `__lt__(self, other)`  | less-than (<)                 |
  | `__le__(self, other)`  | less-than or equal-to (<=)    |
  | `__gt__(self, other)`  | greater-than (>)              |
  | `__ge__(self, other)`  | greater-than or equal-to (>=) |
  | `__eq__(self, other)`  | equal to (==)                 |
  | `__ne__(self, other)`  | not-equal to (!=)             |
  


