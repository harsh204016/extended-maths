# Module: Extended Maths
# Author: Harsh Gupta <harshgupta204016@gmail.com>
# License: MIT
# Release: Extended maths



def factorial(n):
    """
    A function to calculate factorial of a number
    :param n:integer
    """
    if n is None or not isinstance(n , int):
        raise Exception("Entered number is invalid ")
    if n==0:
        return 1
    result=1
    for i in range(2,n+1):
        result*=i
    return result

def isPalindrome(n):
    """
    A function to check if the string is palindrome or not
    :param n:string or intger
    """
    if isinstance(n , int):
        n = str(n)
    return n == n[::-1]

def 

