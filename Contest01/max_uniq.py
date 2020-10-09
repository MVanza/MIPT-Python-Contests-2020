a = {}
lst = list(map(int, input().split()))
for i in lst:
    a[i] = i not in a
print(max(i for i in a if a[i]))
