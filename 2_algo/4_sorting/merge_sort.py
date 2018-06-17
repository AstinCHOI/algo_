def merge(left, right):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)

if __name__ == '__main__':
    arr = [99,2,22,3,1,29,42,321,8,4,23]
    print(merge_sort(arr))


## example
# [3, 1, 4, 2, 5]

# devide1, left
# 3, 1

# devide2, left
# 3

# devide2, right
# 1

# merge2
# 1, 3

# devide1, right
# 4, 2, 5

# devide3, left
# 4, 2

# devide4, left
# 4

# devide4, right
# 2

# merge4
# 2, 4

# devide3, right
# 5

# merge3
# 2, 4, 5

# merge1
# 1, 2, 3, 4, 5
