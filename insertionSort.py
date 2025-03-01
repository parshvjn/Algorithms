a = [5,0,6,7,3,4,6,8,2,1,2,3,4,0,-1, -5,2,3,-8, -10, 4]

n = len(a)
combs = []

for i in range(1, n):
    key = a[i]
    j = i-1
    while j>=0 and a[j] > key:
        combs.append(1)
        a[j+1] = a[j]
        j = j-1
    a[j+1] = key

print(a)
print(len(combs))