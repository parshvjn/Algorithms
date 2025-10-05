def maxHeap(array, heapSize, i):
    left = 2*i + 1
    right = 2*i+2
    largest = i
    if left < heapSize and array[left] > array[largest]:
        largest = left
    if right < heapSize and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        maxHeap(array, heapSize, largest)

def minHeap(array, i):
    left = 2*i + 1
    right = 2*i+2
    smallest = i
    if left < len(array) and array[left] < array[smallest]:
        smallest = left
    if right < len(array) and array[right] < array[smallest]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        minHeap(array, i) # i / smallest

def heapSort(array):
    heapSize = len(array)
    for i in range(heapSize//2-1, -1, -1):
        maxHeap(array, heapSize, i)
    for i in range(heapSize-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        maxHeap(array, i, 0)



if '__main__':
    array = [2,8,5,3,9,1]
    heapSort(array)
    print(array)