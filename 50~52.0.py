# 52
n = bool(int(input()))
print(n)

# 53
n = bool(int(input()))
print(not n)

# 54
a, b = map(int, input().split())
print(bool(int(a)) and bool(int(b)))
# 55
a, b = map(int, input().split())
print(bool(int(a)) or bool(int(b)))

56
a, b = map(int, input().split())
print((bool(a) and not (bool(b))) or (bool(b) and not (bool(a))))

57

a, b = map(int, input().split())
print((bool(a) and bool(b)) or (not (bool(a) and not (bool(b)))))

58
a, b = map(int, input().split())
print(bool(a) == bool(b) == False)
