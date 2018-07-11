result = []
g = []
N = int(input())
a = [i for i in range(2, 10)]
while N != 1:
    i = 0
    if N % a[i] == 0:
        g += str(a[i])
        N /= a[i]
        i += 1
    else:
        result = "-1"
else:
    result = "-1"
print(g)
print(result)
