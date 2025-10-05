
def partition(array, low, high): # normal way that can run in any language like c++ (core logic)
    pivot = array[low]
    i, j, = low, high
    while i < j:
        while i <= high and array[i] <= pivot:
            i += 1
        while j>= low and array[j] > pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]
    array[low], array[j] = array[j], array[low]
    return j

def quickSort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quickSort(array, low, p-1)
        quickSort(array, p+1, high)
    return array

# Faster way to write in quick sort format
def quickSortListComp(arr:list): #  inplace still i think (pythonic way)
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quickSortListComp(left) + [pivot] + quickSortListComp(right)

if '__main__':
    arr = [2,3,1,4,23,4]
    # print(quickSort(arr, 0, len(arr)-1)) #inpalce
    # print(arr)
    
    print(quickSortListComp(arr)) # inplace (still uses saem array even though it doesn't actually change the variable to use), not stable (switches the same type of number), not adaptive (has diff timecpmlexity)