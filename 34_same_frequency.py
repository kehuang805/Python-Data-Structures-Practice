from collections import Counter


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num1Counter = Counter(str(num1))
    num2Counter = Counter(str(num2))

    return num1Counter == num2Counter
