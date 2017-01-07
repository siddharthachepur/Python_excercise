# Solution 1 with recursion, works with smaller number
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Solution 2 with recursion and storing in memory, works with slightly higher number
fib_mem = {0: 0, 1: 1}
def fibm(n):
    if n not in fib_mem:
        fib_mem[n] = fib(n-1) + fib(n-2)
    return fib_mem[n]


# Solution 3, works best with smaller or higher numbers
def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
