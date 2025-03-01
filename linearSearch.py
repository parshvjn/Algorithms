a = [1,3,2,6,7,8,3]

key = 600

for x in a:
    if x == key:
        print('Found it at index ', a.index(x))
        break
    else:
        print('key not found')
        