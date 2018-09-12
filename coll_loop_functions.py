

def fizz_buzz_sum(numbers, exclude=False):
    '''Sums all numbers in a list that are either a multiple of 3 or 5.

    Parameters
    ----------
    numbers: list
      A list of integers.

    Returns
    -------
    sum: int
      The sum of all the numeric data in the list, excluding those summands
      divisible by 3 or 5.
    '''
    result = 0
    if exclude == True:
        for i in numbers:
            if (i%3 != 0) and (i%5 != 0):
                result += i
    else:
        for i in numbers:
            if (i%3 == 0) or (i%5 == 0):
                result += i
    return result




def make_triangle(n):
    '''Make a triangle containing the integers from 0 to (n+1)*n / 2

    $ make_triangle(2)
    [[1], [2, 3]]
    $ make_triangle(3)
    [[1], [2, 3], [4, 5, 6]]

    Parameters
    ----------
    n: positive integer

    Returns
    -------
    triangle: list of lists of integers
      A triangle continaing the consecutive integers
    '''

    if n <= 0:
        raise ValueError('you entered a non-positive value')
    triangle = []
    a = 1
    for i in range(a, n+1):
        triangle.append(list(range(a, a+i)))
        a += i
    return triangle


#def triangle_sum(triangle):
    '''Sum the diagonals of a triangle of numbers.

    $ triangle_sum([[1], [2, 3]])
    [2, 4]

    Because:
    [1]
    [2, 3] <- sum the diagonals
     2  4

    $ triangle_sum([[1], [2, 3], [4, 5, 6]])
    [4, 7, 10]

    Because:
    [1]
    [2, 3]
    [4, 5, 6] <- sum the diagonals
     4  7  10

    Parameters
    ----------
    triangle: list of lists of numbers

    Returns
    -------
    diagonal_sums: list of numbers
      The diagonal sums of the triangle.
    '''
"""
    for i in range(-1, -len(triangle)-1, -1):
        sum = 0
        for row in triangle:
            try:
                sum += row[i]
            except IndexError:
                pass
#            if i < -len(row):
#                sum += row[i]
        result.append(sum)
    result.reverse()
    return result

#   sum = 0
#    for row in triangle:
#        for n in row:
#            sum += n
"""



def main():
    #call the functions and associated code here
    pass

if __name__ == "__main__":
    main()
