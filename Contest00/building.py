myList = list(map(int, input().split()))
N = myList[0]
M = myList[1]
K = int(input())
win = []
allx = []
ally = []
for i in range(K):
    t = list(map(int, input().split()))
    win.append(t)
    allx.append((t[0], t[1]))
    ally.append((t[2], t[3]))


def check_line(mylist):
    for i in mylist:
        k = 0
        for it in i:
            k += 1
            if k <= 2:
                if it > N:
                    return True
            else:
                if it > M:
                    return True
    return False


b = check_line(win)
if b:
    print("broken")
else:
    allx.sort()
    # print(allx)
    xb = True
    ally.sort()
    # print(ally)
    yb = True
    for i in range(K-1):
        if allx[i][1] > allx[i+1][0]:
            if ally[i][1] > ally[i][0]:
                xb = False
                break
    if xb:
        print("correct")
    else:
        print("broken")
