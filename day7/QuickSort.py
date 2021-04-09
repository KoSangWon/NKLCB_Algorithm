# In-place O(logN)
def quick_sort(x):
    def partition(low, high):
        pivot = x[(low + high) // 2]
        while low <= high: # mid에서 만나면 탈출(즉, low == mid인 경우 탈출)
            while x[low] < pivot:
                low += 1
            while x[high] > pivot:
                high -= 1

            if low <= high:
                x[low], x[high] = x[high], x[low]
                low, high = low + 1, high - 1

        return low

    def sort(low, high):
        if high <= low: # 크기가 0, 1인 경우 처리
            return
        
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    return sort(0, len(x) - 1)


# 공간복잡도 O(NlogN)
def quicksort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    left = []
    right = []
    mid = []
    for a in x:
        if a < pivot:
            left.append(a)
        elif a > pivot:
            right.append(a)
        else:
            mid.append(a)

    return quicksort(left) + mid + quicksort(right)