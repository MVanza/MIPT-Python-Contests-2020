n = int(input())
fib = [0]*8 + [1]
for i in range(9, n):
    fib.append(fib[i-2]+fib[i-1]+fib[i-3]+fib[i-4]+fib[i-5]+fib[i-6]+fib[i-7]+ fib[i-8]+ fib[i-9])
print(fib[n-1])
