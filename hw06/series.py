def fibonacci(n):
    """Returns the the value of the nth number in the fibonacci sequence"""
    first_num = 0
    second_num = 1
    nth = 0
    if(n <= 1):
        return first_num
    elif(n == 2):
        return second_num
    else:
        for i in range(n - 2):
            nth = first_num + second_num
            first_num = second_num
            second_num = nth
    return nth


def lucas(n):
    """Returns the the value of the nth number in the lucas numbers sequence"""
    first_num = 2
    second_num = 1
    nth = 0
    if(n <= 1):
        return first_num
    elif(n == 2):
        return second_num
    else:
        for i in range(n - 2):
            nth = first_num + second_num
            first_num = second_num
            second_num = nth
    return nth


def sum_series(n, num1=0, num2=1):
    """Returns the nth value of user provided sum strings. Defaults to
     Fibonacci."""
    first_num = num1
    second_num = num2
    nth = 0
    if(n <= 1):
        return first_num
    elif(n == 2):
        return second_num
    else:
        for i in range(n - 2):
            nth = first_num + second_num
            first_num = second_num
            second_num = nth
    return nth


if __name__ == "__main__":
    # Test to make sure the fibonacci function returns the eigth number
    # of the series correctly.
    assert fibonacci(8) == 13
    # Test to make sure the lucas function returns the eigth number
    # of the series correctly.
    assert lucas(8) == 29
    # Test to make sure the sum_series function returns the eigth number
    # of the series correctly.
    assert sum_series(8, 5, 6) == 118
