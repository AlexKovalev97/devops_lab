result = []
N = int(input())
if N == 1:
    result = "-1"
else:
    while N != 1:
        i = 9
        while i < 10:
            if N % i == 0:
                result += str(i)
                N /= i
            i -= 1
print(result)
