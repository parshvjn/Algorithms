
def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def mergeSort(a):
    if len(a) <= 1: return a

    mid = len(a)//2
    lefth = a[:mid]
    righth = a[mid:]
    print(lefth, righth)
    sortedLeft = mergeSort(lefth)
    sortedRight = mergeSort(righth)
    print(sortedLeft, sortedRight)
    return merge(sortedLeft, sortedRight)

if "__main__":
    array = [2, 1,4,6,2,3,10,23,1,13]
    print(mergeSort(array))