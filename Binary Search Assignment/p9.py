# Valid Perfect Square



def isPerfectSquare(n):
    sum = 0
    i = 1
    while sum < n:
        sum += i
        i += 2
        if sum == n:
            return True
    return False


num = 16
print(isPerfectSquare(num))