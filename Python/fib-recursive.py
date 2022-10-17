import time
import itertools

# Recursive Fibonacci Sequence
def recursiveFib(n):
    return n if n < 2 else recursiveFib(n-1) + recursiveFib(n-2)

start_time = time.time()
for _, i in itertools.product(range (1000), range(25)):
    recursiveFib(i)
    
print(f"--- {time.time() - start_time} seconds ---")
