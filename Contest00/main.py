myList = list(input().split())
N = int(myList[0])
M = int(myList[1])
K = int(myList[2])
Ta = float(myList[3])
Tb = float(myList[4])
Tc = float(myList[5])
eltime = abs(K - N) * Ta + 3 * Tb + abs(M-N) * Ta  # Время лифта
sttime = abs(M-N) * Tc  # Время лестницы
if sttime < eltime:
    print("stairs")
else:
    print("elevator")
