name = str(input())
with open(name) as f:
    m = ''
    s = 0
    for i in f:
        for it in i.split():
            if len(it) > s:
                s = len(it)
                m = it
    print(m)
