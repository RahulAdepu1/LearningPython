## GCD (Greattes common Divisor) of two numbers using recursion?

# Using Euclidean Algorithm
'''
(12,8) -> (12/8) = Q is 0, Rem is 4
(8,4) -> (8/4) = Q is 2, Rem is 0
'''
import math

def gcd(a,b):
    assert int(a) == a and int(b) == b, "Error"
    a = abs(a)
    b = abs(b)

    if b > a:
        a,b = b,a
    if b > 0:
        return gcd(b, a%b)
    return a

print(gcd(-18,-48))