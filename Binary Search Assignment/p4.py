# First Bad Version


def first_bad_version(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

def isBadVersion(version):
    bad_version = 4
    return version >= bad_version

n = 1
print(first_bad_version(n))