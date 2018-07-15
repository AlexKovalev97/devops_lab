a = int(input('Input size of A: '))
b = int(input('Input size of B: '))
A = []
B = []
raw = []
cnt = 0
for i in range(a):
    A.append(input('A = '))

for i in range(b):
    B.append(input('B = '))
l_a = len(str(a))
l_b = len(str(b))
if l_a <= 10000 and l_b <= 100:
    for i in range(b):
        for j in range(a):
            l_A = len(A[j])
            l_B = len(B[i])
            if B[i] == A[j] and l_A <= 100 and l_B <= 100:
                raw.append(str(j + 1))
                cnt = 1
        if cnt == 1:
            print(" ".join(str(r) for r in raw))
            raw.clear()
            cnt = 0
        else:
            print(-1)
