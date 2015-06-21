def fibonacci(n=0):
    """Returns the the value of the nth number in the fibonacci sequence"""
    nth = 0
    for i in range(n):
        if(nth == 0):
            nth += 1
        else:
            nth += nth
    return nth
