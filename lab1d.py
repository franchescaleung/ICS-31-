# Franchesca Amanda Leung 78831208 and Dong Zou 53574913.   ICS 31 Lab sec 3. Lab Assignment 1d.

def factorial (n: int) -> int:
    '''Compute n! (n factorial)'''
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)
assert factorial(0) == 1
assert factorial(5) == 120

print("10! is", factorial(10))
print("100! is", factorial(100))
print("(50 * 10)! is", factorial(50*10))
print("120! is", factorial(120))
print("factorial of 5!", factorial(factorial(5)))
'''
print("factorial of 50!", factorial(factorial(50))) #gives error

'''
