# Fibonacci Number using recursion

def fib(num):
    assert num >=0 and int(num) == num, 'The number must be positive integer only'
    if num in [0,1]:
        return num
    return fib(num-1) + fib(num-2)

print(fib(10))