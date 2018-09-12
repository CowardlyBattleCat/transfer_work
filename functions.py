

def f(x):
    """Just a first function to help us test assert"""
    return x + 1

def sum_whole_numbers(x):
    """A function that returns the sum of the whole numbers between 1 and a specified number."""
    sum_result = 0
    i = 1
    while i <= x:
        sum_result += i
        i += 1
    return sum_result

def sign(x):
    """A function that takes a specified number and returns 1 if it is positive, -1 if it is negative, and 0 if it is zero."""
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

def is_larger_than(a, b):
    """A function that takes two numbers, a and b, and returns True if the first number is larger or False if it's not."""
    if a > b:
        return True
    else:
        return False

def sum_whole_numbers_descend(x):
    """A function that computes the sum from 0 to a specified number, starting at the specified number and working down."""
    sum_result = 0
    i = x
    while i > 0:
        sum_result += i
        i -= 1
    return sum_result

def factorial(x):
    """A function that computes the factorial of a specified number."""
    if (type(x) == float) and (x.is_integer == False):
        raise TypeError('factorials of non-integer numbers are beyond the scope of this function')
    elif type(x) != int:
        raise TypeError('input must have type int')
    elif x < 0:
        raise ValueError('factorial is not defined for negative integers')
    else:
        factorial = 1
        i = x
        while i > 1:
            factorial *= i
            i -= 1
        return factorial

def divisor(x):
    """A function that computes and returns all of the divisors of a specified number."""
    if type(x) != int:
        raise TypeError('input must have type int')
    if x == 0:
        raise ValueError('cannot return all values--every integer is a divisor of 0')
    else:
        x = abs(x)
        divisors = [1, -1]
        for i in range(2, (int((x/2)+1))):
            if x%i == 0:
                divisors.insert(0, i)
                divisors.append(-i)
        divisors.insert(0, x)
        divisors.append(-x)
        return divisors




def main():
    #call the functions and associated code here
    pass

if __name__ == "__main__":
    main()
