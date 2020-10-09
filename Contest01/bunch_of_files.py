a = []
for i in input().split():
    try:
        with open(i) as f:
            for i in f.readlines():
                j = i.split()
                a += j
    except:
        pass

s = set(a)
a = list(s)
a.sort()
print(*a)
