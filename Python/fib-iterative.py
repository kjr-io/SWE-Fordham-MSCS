import time
import itertools

# Iterative Fibonacci Sequence
def iterativeFib(n):
    if n < 2:
        return n

    a = 0
    b = 1
    i = 0
    
    while i < n:
        temp = a
        a = b
        b = temp + b
        i += 1
        
    return a

start_time = time.time()
for _, i in itertools.product(range (10000000), range(25)):
    iterativeFib(i)

print(f"--- {time.time() - start_time} seconds ---")