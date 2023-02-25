## Sum of digits of a number

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "Error"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n / 10))

print(sumOfDigits(89))