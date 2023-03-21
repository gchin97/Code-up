sum = int(input())
i = 0
s = 0
while sum > s:
    i += 1
    s = s+i
print(i)


def positive(x):
    return x > 0


a = list(filter(positive, [1, -3, 4, 5, 6]))
print(a)


def two_times():
    return a*2


a = list(map(two_times, [1, 2, 3, 4]))
print(a)

a = list(map(lambda x: x*2, [1, 2, 3, 4]))
print(a)
