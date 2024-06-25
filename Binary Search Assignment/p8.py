# Find First and Last Position in Sorted Array


def search(nums, x):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < x:
                left = mid + 1
            else:
                right = mid
        return left

def searchRange(nums, target):
    
    l = search(nums, target)
    r = search(nums, target + 1)
    
    if l == len(nums) or nums[l] != target:
        return [-1, -1]
    else:
        return [l, r - 1]

nums = [5,7,7,8,8,10]
target = 8

print(searchRange(nums, target))