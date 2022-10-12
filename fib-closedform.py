# Closed Form Fibonacci Sequence
# Solution Based on: http://mathonline.wikidot.com/a-closed-form-of-the-fibonacci-sequence
def closedFormFib(n):
    # n Exists in the Series Provided in Theorum I
    try:
        if n < 0:
            return("Sorry, the Number is Not in the Series!")
        closedFormEq = (1/(5 ** 0.5)) * ( (((1+(5 ** 0.5))/2)**n) - (((1-(5 ** 0.5))/2)**n) )
        return int(closedFormEq)
    except:
        return("Sorry, Not a Valid Input!")