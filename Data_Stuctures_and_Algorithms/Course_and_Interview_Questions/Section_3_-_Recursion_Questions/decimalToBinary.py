# Convert a decimal number to binary usinf recursion

def d2b(n):
    assert int(n) == n, "Error"
    if n == 0:
        return 0
    else:
        return n % 2 + (10 * d2b(int(n / 2)))


print(d2b(13))