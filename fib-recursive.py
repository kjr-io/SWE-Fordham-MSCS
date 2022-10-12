# Recursive Fibonacci Sequence
def recursiveFib(n):
    # Filtering Invalid Inputs
    if type(n) != int or n < 0:
        return("Sorry, Not a Valid Input!")

    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursiveFib(n - 1) + recursiveFib(n - 2)
