# Recuresive Functions

* Definition: A function that calls itself is known as a recursive function

* Example:
  ```
  def count_down(count):
      if count == 0
          print('Go!')
      else:
          print(count)
          count_down(count-1)
  
  count_down(2)
  ```

## Creating a recursive function

### Two steps to create a recursive function

1. Write base case 
   * Write the case that returns a value without performing a recursive call
   * Write that part of the function first and then test
 
2. Write recursive case
   * Add the recursive case to the function
 
### Common Errors

1. Not covering all possible base cases in a recursive function
2. Writing a recursive function that doesn't always reach a base case

## Recursive Math Functions


