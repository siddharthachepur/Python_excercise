
def fib(n):
     if n == 0:
         return 0
     elif n == 1:
         return 1
     else:
         return fib(n-1) + fib(n-2)


fib_mem = {0:0, 1:1}
def fibm(n):
    if n not in fib_mem:
        fib_mem[n] = fib(n-1) + fib(n-2)
    return fib_mem[n]