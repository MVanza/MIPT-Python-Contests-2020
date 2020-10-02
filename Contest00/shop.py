N = int(input())
myList = []
for i in range(N):
    n = tuple(map(int, input().split()))
    myList.append(n)
S = int(input())
myList.sort()
p = 0
k = 0
can = 0
for i in myList:
    p += i[0]
    k += 1
    can += i[1]
    if p >= S:
        if p == S:
            break
        else:
            k -= 1
            can -= i[1]
            break
print(k, can)
