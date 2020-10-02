def sumel(n):
    mysum = 0
    for i in n:
        mysum += int(i)
    return mysum


N = input()
mySum = N
while len(str(mySum)) != 1:
    mySum = sumel(str(mySum))
print(mySum)
