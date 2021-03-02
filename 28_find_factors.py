def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    i = 1
    factors1 = []
    factors2 = []
    while i <= num**0.5:
        if num % i == 0:
            factors1.append(i)
            factors2.append(num//i)
        i += 1

    return factors1 + factors2[::-1]
    