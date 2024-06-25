# Sqrt(x)



def mySqrt(x):
    l = 1
    r = x + 1

    while l < r:
        m = (l + r) // 2
        if m > x // m:
            r = m
        else:
            l = m + 1

    return l - 1

x = 4
print(mySqrt(x))