import math

def factorial_calc(n):
    """Function that calculates the factorial value
    param: n: int
    return: result: int"""
    if type(n) != int:
        raise TypeError("The input value for factorial calculation must an integer")
    
    elif n < 0 :
        raise ValueError("The input value for factorial calculation can't be negative")
    
    result = math.factorial(n)
    print(f"The factorial of {n} is {result}")
    return result
