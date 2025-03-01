# a = [5,0,6,7,3,4,6,8,2,1,2,3,4,0,-1, -5,2,3,-8, -10, 4]
a = [1,2,3,4]
a = [3,4,1,2]
a = [64, 25, 12, 22, 11]
a = [5,0,6,7,3,4,6,8,2,1,2,3,4,0,-1, -5,2,3,-8, -10, 4]
# a = [1,2,3,4,5,6,7,8,9,10]

n = len(a)
combs = []

for i in range(0, n-1):
    for j in range(i+1, n):
        min1 = a[i]
        if a[j] < min1:
            a[i], a[j] = a[j], a[i]
        combs.append([a[i], a[j]])
        print(a)


print(a)
print(len(combs))