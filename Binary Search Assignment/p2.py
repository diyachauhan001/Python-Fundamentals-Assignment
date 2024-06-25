# Binary Search in a 2D array


def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return (-1, -1)
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_val = matrix[mid // cols][mid % cols]
        
        if mid_val == target:
            return (mid // cols, mid % cols)
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return (-1, -1)

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
print(search_matrix(matrix, target))
