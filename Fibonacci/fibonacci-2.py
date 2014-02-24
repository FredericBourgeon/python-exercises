########################################
## Fibonacci sequence
## Returns the nth term
## Simple recursive algorithm
########################################

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
