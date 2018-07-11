a = list(map(int, input().split(", ")))
b = list(map(int, input().split(", ")))
print("result =", list(set(a) & set(b)))
