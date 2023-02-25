# Power of a number

def power(base, exponent):
    assert int(exponent) == exponent, "Error"
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1/base * power(base, exponent+1)
    else:
        return base * power(base, exponent-1)

    power(2, 0)  # 1
    power(2, 2)  # 4
    power(2, 4)  # 16