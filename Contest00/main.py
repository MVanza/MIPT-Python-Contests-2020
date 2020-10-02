N = int(input())
myListp = []
myListm = []
for i in range(N):
    n = int(input())
    if n < 0:
        myListm.append(n)
    else:
        myListp.append(n)
myListp.sort()
myListm.sort(reverse=True)
myList = myListp + myListm
print(*myList)
