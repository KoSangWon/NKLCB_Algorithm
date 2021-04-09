# def solution(array, target_value, start, end):
#     array.sort()
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target_value:
#         return mid
#     elif array[mid] > target_value:
#         return solution(array, target_value, start, mid - 1)
#     else:
#         return solution(array, target_value, mid, end)
    
# print(solution([1,2,3,4],2,0,3))


def solution(array, target_value):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if target_value < array[mid]:
            right = mid - 1
        elif target_value > array[mid]:
            left = mid + 1
        else:
            return mid  
    return -1

def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        

    return binary_search_recursion(target, start, end, data)


