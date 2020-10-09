lst = input().split()
s = set()
for i in lst:
    s.add(i)
a = []
for i in s:
    a.append((lst.count(i), i))
a.sort(key=lambda x: (-x[0], x[1]))
for i in a:
    print(*i)
