# Binary Search to find the floor and ceil of an element in an array


def find_floor_and_ceil(nums, target):
    left, right = 0, len(nums) - 1
    floor, ceil = -1, -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return (nums[mid], nums[mid])
        elif nums[mid] < target:
            floor = nums[mid]
            left = mid + 1
        else:
            ceil = nums[mid]
            right = mid - 1
            
    return (floor, ceil)

nums = [1, 2, 8, 10, 10, 12, 19]
target = 5
print(find_floor_and_ceil(nums, target))