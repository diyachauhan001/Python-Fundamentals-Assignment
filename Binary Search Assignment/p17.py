# Kth Positive Missing Number


def find_kth_positive(arr, k):
    l = 0
    r = len(arr)

    while l < r:
        m = (l + r) // 2
        if arr[m] - m - 1 >= k:
            r = m
        else:
            l = m + 1

    return l + k

arr = [2,3,4,7,11]
k = 5

print(find_kth_positive(arr, k))