# Peak Index in Mountain Array



def find_peak_element(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        m = (l + r) // 2
        if nums[m] >= nums[m + 1]:
            r = m
        else:
            l = m + 1

    return l

nums = [1,2,3,1]
print(find_peak_element(nums))