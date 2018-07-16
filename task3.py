N = int(input())
print("N " + str(N))

result = ''

while N >= 10:
    i = 9
    while i < 10:
        if N == 1 or i == 1:
            break
        if N % i == 0:
            result += str(i)
            N /= i
            i = 10
        i -= 1
    if N == 1 or i == 1 or N > 10**9:
        break

if not result or N > 10:
    result = -1

if 1 < N < 10:
    result = str(N)

if int(result) > 0:
    if int(result[::-1]) < int(result):
        result = result[::-1]

print(result)
