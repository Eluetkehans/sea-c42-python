def fibonacci(n):
    """Returns the the value of the nth number in the fibonacci sequence"""
    first_num = 0
    second_num = 1
    nth = 0
    if(n <= 1):
        return first_num
    else:
        for i in range(n - 1):
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

nth = lucas(int(input("number: ")))
print(nth)
