def fibonacci(n=0):
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

nth = fibonacci(int(input("number: ")))
print(nth)
