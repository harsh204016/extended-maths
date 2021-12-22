# Module: Extended Maths
# Author: Harsh Gupta <harshgupta204016@gmail.com>
# License: MIT
# Release: Extended maths

from large_multiplication import multiply

def factorial(number):
    """
    A function to calculate factorial of a number.

    :param number:integer
    """
    if number is None or not isinstance(number , int):
        raise Exception("Entered number is invalid ")
    if number == 0:
        return 1
    result=1
    if number < pow(2,20):
        for iter in range(2,number+1):
            result = result*iter

    elif number >= pow(2,5):
        for iter in range(2,number+1):
            result = multiply(result,iter)
    return result

def isPalindrome(number):
    """
    A function to check if the string is palindrome or not.
    :param number:string or intger
    """
    if isinstance(number , int):
        number = str(number)
    return number == number[::-1]


