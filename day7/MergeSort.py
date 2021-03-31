def merge_sort(x, low=0, high=-1, arr=None):
    if high == -1:
        high = len(x) - 1
    if arr is None:
        arr = [0] * len(x)

    if low >= high:
        return

    mid = (low + high) // 2
    merge_sort(x, low, mid, arr)
    merge_sort(x, mid + 1, high, arr)

    # merge
    i, j = low, mid + 1 # 양쪽의 시작점
    for k in range(low, high + 1):
        if j > high:
            arr[k] = x[i]
            i += 1
        elif i > mid:
            arr[k] = x[j]
            j += 1
        elif x[i] <= x[j]: # 정상범위, 등호는 없어도 됨
            arr[k] = x[i]
            i += 1
        else:
            arr[k] = x[j]
            j += 1

    x[low:high+1] = arr[low:high+1]


x = [5, 25, 6, 2, 3, 7]
merge_sort(x, 0, len(x)-1, [0]*len(x))
print(x)
    
    
def merge_sort2(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left1 = merge_sort2(left)
    right1 = merge_sort2(right)
    return merge(left1, right1)

def merge(left, right):
    i = 0
    j = 0 
    sorted_list = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left): # 남은 값들 넣어주기
        sorted_list.append(left[i])
        i += 1

    while j < len(right): # 남은 값들 넣어주기
        sorted_list.append(right[j])
        j += 1

    return sorted_list

print(merge_sort2([2,3,1,4,6,5]))
