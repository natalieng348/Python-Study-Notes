"""
6.23 LAB: Fibonacci sequence
IS 640 - Natalie Nguyen

The Fibonacci sequence begins with 0 and then 1 follows.
All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13.

Complete the fibonacci() function, which has an index n as parameter,
and returns the nth value in the sequence. Any negative index values should return -1.

Note: Use a for loop and DO NOT use recursion.
"""

def fibonacci(n):
    """Take index n as a parameter and return the nth value in the sequence"""
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        num = [0, 1]
        for index in range(n):
            if index == (n-1):
                break
            else:
                sum = num[index] + num[index + 1]
                num.append(sum)
        result = num[-1]
        return result
            

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')