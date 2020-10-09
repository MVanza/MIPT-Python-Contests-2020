import os


def check_dir(path):
    d = os.listdir(path)
    j = 0
    f = 0
    for i in d:
        if os.path.isfile(path + "/" + i):
            j += 1
        else:
            p, k = check_dir(path + "/" + i)
            j += p
            f += k
    return j, f + 1


n = str(input())
if os.path.exists(n):
    if os.path.isfile(n):
        print("Files:", 1)
        print("Dirs:", 0)
    else:
        j, f = check_dir(n)
        print("Files:", j)
        print("Dirs:", f)
else:
    print("Files:", 0)
    print("Dirs:", 0)
