a = [5,0,6,7,3,4,6,8,2,1,2,3,4,0,-1, -5,2,3,-8, -10, 4]
n = len(a)
comparisons = []
for i in range(n-1):
    swap = False
    for j in range(n-1):
        comparisons.append([a[j], a[j + 1]])
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swap = True
    if not swap:
        break

print(a)
print(len(comparisons))