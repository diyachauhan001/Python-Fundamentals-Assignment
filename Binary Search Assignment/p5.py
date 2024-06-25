# Guess Number Higher or Lower



target = 6
def guess(num):
    if num < target:
        return 1
    elif num > target:
        return -1
    else:
        return 0

def guessNumber(n):
    low = 1
    high = n
    while low <= high:
        mid = low + (high - low) // 2
        g = guess(mid)
        if g == -1:
            high = mid - 1
        elif g == 1:
            low = mid + 1
        else:
            return mid
    return mid

n = 10
pick = 6

print(guessNumber(n, pick))