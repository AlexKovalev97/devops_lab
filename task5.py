n = int(input())
i = 1
while True:
    if n >= 0 and n.bit_length() < 33:
        while i <= n.bit_length():
            i <<= i
        print(n ^ (i - 1))
        break
    else:
        print("Error. Try one more time")
        n = int(input())
        continue
