# Find in Mountain Array



class MountainArray:
    def __init__(self, arr):
        self.array = arr
    
    def get(self, index):
        return self.array[index]
    
    def length(self):
        return len(self.array)

def find_in_mountain_array(target, mountain_arr):
    n = mountain_arr.length()
    peak_index = peak_index_in_mountain_array(mountain_arr, 0, n - 1)
    
    if mountain_arr.get(peak_index) == target:
        return peak_index
    
    left_index = search_left(mountain_arr, target, 0, peak_index)
    if left_index < n and mountain_arr.get(left_index) == target:
        return left_index
    
    right_index = search_right(mountain_arr, target, peak_index + 1, n - 1)
    if right_index < n and mountain_arr.get(right_index) == target:
        return right_index
    
    return -1

def peak_index_in_mountain_array(A, l, r):
    while l < r:
        m = (l + r) // 2
        if A.get(m) < A.get(m + 1):
            l = m + 1
        else:
            r = m
    return l

def search_left(A, target, l, r):
    while l < r:
        m = (l + r) // 2
        if A.get(m) < target:
            l = m + 1
        else:
            r = m
    return l

def search_right(A, target, l, r):
    while l < r:
        m = (l + r) // 2
        if A.get(m) > target:
            l = m
        else:
            r = m - 1
    return l

# Example usage:
array = MountainArray([1, 2, 3, 4, 5, 3, 1])
target = 3
print(find_in_mountain_array(target, array))
