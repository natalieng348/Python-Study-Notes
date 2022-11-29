# Chapter 16: Searching and Sorting Algorithms

## 1. Searching and algorithms

### Algorithms and linear search

* Algorithm is a sequence of steps for accomplishing a task.

* Linear search is a search algorithm that starts from the beginning of a list and checks each element until the search key is found, or the end of the list is reached.

### Algorithm runtime

* Algorithm runtime is the time the algorithm takes to execute.


## 2. Binary Search

### Using binary search

* Linear seach can lead to long runtimes since it requires searching all list elements. 
* A faster search, known as binary search, checks the middle contact first. If the desired value comes before the middle contact, binary search will then search the first half and otherwise, the last half. 

### Binary seach algorithm

* Binary search is a faster algorithm for searching a list of the list's elements are sorted and directly accessible (such as list)

## 3. O notation

### Big O notation

* Big O notation is a mathematical way of describing how a function (running time of an algorithm) generally behaves in relation to the input size.
* Rule 1: 
  * If f(x) is a sum of several terms, the highest order term is kept and others are discarded. 
* Rule 2:
  * If f(x) has a term that is a product of several factors, all constants are omitted.

### Rule for determining Big O notation of composite functions

![image](https://user-images.githubusercontent.com/96028654/204662015-8e3b7b7a-4159-4f35-994c-46d1dfd602fa.png)

* Note: the logarithm base does not affect the growth rate, so the base is omitted in Big O notation. 
  * Converting from one logarithm base to another base involves a constant factor, which can be simplified in Big O notation
  * Example: O(log2N) = O(logN/log2) = O(logN * 1/log2) = O(logN)
 
### Runtime growth rate

Growth rate for different input sizes:

![image](https://user-images.githubusercontent.com/96028654/204662443-dafd1a29-e9e4-4dbf-adff-33e8642e4132.png)

### Common Big O complexities

Runtime complexities for various code examples:

![image](https://user-images.githubusercontent.com/96028654/204662560-e2dd3f52-6e65-4fcb-ae23-38952926c5a1.png)

## 4. Sorting

* Sorting is the process of converting a list of elements into ascending (or descending) order.

### Selection sort algorithm

* Selection sort is a sorting algorithm that treats the input as two parts, a sorted part and an unsorted part, and repeatedly selects the proper next value to move from the unsorted part to the end of the sorted part.

* 


