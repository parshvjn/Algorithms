from array import array

# arr = array('i', [1,2,3,4,5,6])
# print(arr)

# arr2 = array("I", [1,2,3])
# arr3 = array("L", [1,2,3])

# print(arr.typecode)
# print(type(arr))
# print(arr.buffer_info())
# print(arr3.buffer_info())


# # arr[0] = 'w'

arr = array('f', [1.1,3.3,4.7,8.9, 10.2])
arr1 = array('i', [1,3,5,7,8])

# print(arr + arr1) # doesn't work because they are diff data types

# 1D array memory calculator:
BaseAddress = int(input('BA: '))
A = ['a', 'b', 'c']
dataType = type(A[0])
if dataType == int:
    bytesNum = 2
elif dataType == str:
    bytesNum = 1
elif dataType == float:
    bytesNum = 4

index = int(input("index: "))

print(f'Adress: {BaseAddress + (index * bytesNum)}')