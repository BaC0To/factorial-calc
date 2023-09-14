def factorial_calc_non_recursive(n):
    """A non-recursive function calculator of factorial value
    param: n: int
    return: result: int
    """
    result_factorial = 1
    for item in range(1, n + 1):
        result_factorial = result_factorial * item
    return result_factorial

def factorial_calc_recursive(n):
    """A recursive function calculator of factorial value
    param: n: int
    return: result: int
    """
    return 1 if n in (0, 1) else n * factorial_calc_recursive(n-1)


print(factorial_calc_non_recursive(5))
print(factorial_calc_recursive(5))