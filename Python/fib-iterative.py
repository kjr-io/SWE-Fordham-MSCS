#Iterative Fibonacci Sequence
def iterativeFib(n):
    # Filtering Invalid Inputs
    if type(n) != int or n < 0:
        return("Sorry, Not a Valid Input!")

    ultimate = 0
    current = 1
    i = 1
    while i < n:
        penultimate = ultimate
        ultimate = current
        current = penultimate + ultimate
        i += 1
    return current