71
i = True
while (i):
    n = int(input())
    if (n == 0):
        i = False
else:
    print(n)

72
i = int(input())
while (i > 0):
    print(i)
    i -= 1
73
i = int(input())
while (i > 0):
    print(i-1)
    i -= 1


74
i = ord(input())
n = ord("a")
while i >= n:
    print(chr(n), end=" ")
    n += 1

75
i = int(input())
n = 0
while i >= n:
    print(n)
    n += 1

76
i = int(input())
n = 0
while i >= n:
    print(n)
    n += 1

i = int(input())
for n in range(i+1):
    print(n)

77

i = int(input())
sum = 0
for i in range(i+1):
    if i % 2 == 0:
        print(i)
        sum = sum+i
    print(sum)

78
i = " "
while (i != "q"):
    i = input()
    print(i)

79
sum = input()
i = 0
while sum > i:
    sum = sum+i
    i += 1
    print(i)

sum = int(input())
i = 0
s = 0
while sum > s:
    i += 1
    s = s+i
print(i)

80
n = int(input())
m = int(input())
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)

n, m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        print("{}{}", format(i, j))
