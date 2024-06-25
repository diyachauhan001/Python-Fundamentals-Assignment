# Search Insert Position


def searchInsert(nums, target):
    left = 0
    right = len(nums)
        
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
        
    return left


nums = [1,3,5,6]
target = 5

print(searchInsert(nums, target))