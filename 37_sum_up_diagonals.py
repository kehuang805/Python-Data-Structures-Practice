def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    i = 0
    left_sum = 0
    right_sum = 0
    while i < len(matrix):
        left_sum += matrix[i][i]
        right_sum += matrix[i][len(matrix)-1-i]
        i += 1
    return left_sum + right_sum
    

