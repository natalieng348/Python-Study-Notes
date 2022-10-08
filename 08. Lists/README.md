# Lists

## General

* Accessing a list element: `my_lst[i]` where i is the index of the referenced list item

* Modifying a list and common list operations
  
|           Operation          |                                                            Description                                                           |                           Example code                             |  Example output |
|:----------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------:|:---------------:|
| my_list = [1, 2, 3]          | Creates a list.                                                                                                                  | `my_list = [1, 2, 3] print(my_list)`                               | [1, 2, 3]       |
| list(iter)                   | Creates a list.                                                                                                                  | `my_list = list('123') print(my_list)`                             | ['1', '2', '3'] |
| my_list[index]               | Get an element from a list.                                                                                                      | `my_list = [1, 2, 3] print(my_list[1])`                            | 2               |
| my_list[start:end]           | Get a new list containing some of another list's elements.                                                                       | `my_list = [1, 2, 3] print(my_list[1:3])`                          | [2, 3]          |
| my_list1 + my_list2          | Get a new list with elements of my_list2 added to end of my_list1.                                                               | `my_list = [1, 2] + [3]  print(my_list)`                           | [1, 2, 3]       |
| my_list[i] = x               | Change the value of the ith element in-place.                                                                                    | `my_list = [1, 2, 3] my_list[2] = 9  print(my_list)`               | [1, 2, 9]       |
| my_list[len(my_list):] = [x] | Add the elements in [x] to the end of my_list. The append(x) method (explained in another section) may be preferred for clarity. | `my_list = [1, 2, 3] my_list[len(my_list):] = [9] print(my_list)`  | [1, 2, 3, 9]    |
| del my_list[i]               | Delete an element from a list.                                                                                                   | `my_list = [1, 2, 3] del my_list[1] print(my_list)`                | [1, 3]          |


## List method

* A list method can perform a useful operation on a list such as adding or removing elements, sorting, reversing, etc. 
* Good practice is to use list methods to add and delete list elements as compared to using `del my_list[0]` or `my_list[len(mylist):] = [va'l]` since it yields eaiser-to-read code.

### 1. Adding elements: 

* List method used on `my_list = [5, 8]`

|    List method    |              Description              |           Code example        | Final my_list value |
|:-----------------:|:-------------------------------------:|:-----------------------------:|:-------------------:|
| list.append(x)    | Add an item to the end of list.       | `my_list.append(16)`          | [5, 8, 16]          |
| list.extend([x])  | Add all items in [x] to list.         | `my_list.extend([4, 12])`     | [5, 8, 4, 12]       |
| list.insert(i, x) | Insert x into list before position i. | `my_list.insert(1, 1.7)`      | [5, 1.7, 8]         |


### 2. Removing elements: 

* List method used on `my_list = [5, 8, 14]`

|   List method  |                  Description                  |      Code example      | Final my_list value |
|:--------------:|:---------------------------------------------:|:----------------------:|:-------------------:|
| list.remove(x) | Remove first item from list with value x.     | `my_list.remove(8)`    | [5, 14]             |
| list.pop()     | Remove and return last item in list.          | `val = my_list.pop()`  | [5, 8] val is 14    |
| list.pop(i)    | Remove and return item at position i in list. | `val = my_list.pop(0)` | [8, 14] val is 5    |


### 3. Modifying elements: 

* List method used on `my_list = [14, 5, 8]`

|   List method  |               Description              |     Code example    | Final my_list value |
|:--------------:|:--------------------------------------:|:-------------------:|:-------------------:|
| list.sort()    | Sort the items of list in-place.       | `my_list.sort()`    | [5, 8, 14]          |
| list.reverse() | Reverse the elements of list in-place. | `my_list.reverse()` | [8, 5, 14]          |

### 4. Miscellaneous

|  List method  |                    Description                   |                     Code example                     | Final my_list value |
|:-------------:|:------------------------------------------------:|:----------------------------------------------------:|:-------------------:|
| list.index(x) | Return index of first item in list with value x. | `my_list = [5, 8, 14] print(my_list.index(14))`      | Prints "2"          |
| list.count(x) | Count the number of times value x is in list.    | `my_list = [5, 8, 5, 5, 14] print(my_list.count(5))` | Prints "3"          |


## Iterating over a list

### Built-in function supporting list objects

|  Function |                               Description                              |                    Example code                    | Example output |
|:---------:|:----------------------------------------------------------------------:|:--------------------------------------------------:|:--------------:|
| all(list) | True if every element in list is True (!= 0), or if the list is empty. | `print(all([1, 2, 3]))`<br>`print(all([0, 1, 2]))` | True <br>False |
| any(list) | True if any element in the list is True.                               | `print(any([0, 2]))`<br>`print(any([0, 0]))`       | True <br>False |
| max(list) | Get the maximum element in the list.                                   | `print(max([-3, 5, 25]))`                          | 25             |
| min(list) | Get the minimum element in the list.                                   | `print(min([-3, 5, 25]))`                          | -3             |
| sum(list) | Get the sum of all elements in the list.                               | `print(sum([-3, 5, 25]))`                          | 27             |
