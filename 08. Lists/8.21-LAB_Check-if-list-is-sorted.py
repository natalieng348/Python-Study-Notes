"""8.21 LAB: Check if list is sorted
Natalie Nguyen - IS 604

Write the in_order() function, which has a list of integers as a parameter, 
and returns True if the integers are sorted (from low to high) or False otherwise. 

The program outputs "In order" if the list is sorted, 
or "Not in order" if the list is not sorted.

Ex: If the list passed to the in_order() function is [5, 6, 7, 8, 3], 
then the function returns False and the program outputs:

>> Not in order


Ex: If the list passed to the in_order() function is [5, 6, 7, 8, 10], 
then the function returns True and the program outputs:

>> In order

Note: Use a for loop. DO NOT use sorted() or sort().
"""

def in_order(nums):
    """Return True if list is sorted, and False otherwise"""
    for index in range(len(nums)-1):
        max_num = nums[index]
        next_num = nums[index+1]
        if max_num <= next_num:
            max_num = next_num 
            result = True
        else:
            result = False
            break
    return result
    
if __name__ == '__main__':
    """Test out-of-order example"""
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
        
"""
1: Unit test where nums is [5, 6, 7, 8, 3]
Test passed: in_order() correctly returned False

2: Unit test where nums is [5, 6, 7, 8, 10]
Test passed: in_order() correctly returned True

3: Unit test where nums is [5, 5, 6, 6, 6, 7, 8, 10, 10, 10, 10]
Test passed: in_order() correctly returned True
"""
