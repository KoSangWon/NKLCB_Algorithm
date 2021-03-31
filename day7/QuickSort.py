def quick_sort(x, low, high):
    if high <= low:
        return

    pivot = x[low]
    i, j = low, high

    while i < j:
        while j > low:
            if x[j] < pivot:
                break
            j -= 1
            
        while i < high:
            if x[i] > pivot:
                break
            i += 1
        
        if i < j:
            x[i], x[j] = x[j], x[i]
    
    x[low], x[j] = x[j], x[low]
    
    quick_sort(x, 0, j - 1)
    quick_sort(x, j + 1, high)

x = [5,4,3,1,2,6,3]
quick_sort(x, 0, len(x)-1)
print(x) # [1, 2, 3, 3, 4, 5, 6]