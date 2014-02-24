########################################
## Fibonacci sequence
## Returns the first n terms
## Simple algorithm
########################################

def fib(n):
    a, b = 0, 1
    i  = 0
    while i < n:
        print a
        a, b = b, a + b
        i += 1