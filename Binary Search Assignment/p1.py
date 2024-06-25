# Binary Search


def search( nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left if nums[left] == target else -1

nums = [-1,0,3,5,9,12]
target = 9

print(search(nums, target))