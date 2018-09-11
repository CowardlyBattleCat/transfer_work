def f(x):
    return x + 1

def sum_whole_numbers(x):
    sum_result = 0
    i = 1
    while i <= x:
        sum_result += i
        i += 1
    return sum_result

def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

def is_larger_than(a, b):
    if a > b:
        return True
    else:
        return False

def sum_whole_numbers_descend(x):
    sum_result = 0
    i = x
    while i > 0:
        sum_result += i
        i -= 1
    return sum_result

def factorial(x):
    if type(x) == float and x.is_integer == False:
        raise TypeError('factorials of non-integer numbers are beyond the scope of this function')
#    elif
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
    x = abs(x)
    divisors = [1, -1]
    if x == 0:
        return ValueError('cannot return all values--every integer is a divisor of 0')
    else:







def main():
    #call the functions and associated code here
    pass

if __name__ == "__main__":
    main()
