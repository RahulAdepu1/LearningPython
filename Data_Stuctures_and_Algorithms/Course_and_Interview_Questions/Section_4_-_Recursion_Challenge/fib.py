# Fibonacci Series

def fib(num):
    if num in [0,1]:
        return num
    return fib(num-1) + fib(num-2)

print(fib(4)) # 3
print(fib(10)) # 55
print(fib(28)) # 317811
print(fib(35)) # 9227465