80
n = input()
for i in range(1, 16):
    print('%x*%x=%x'.upper() %
          (int(n, 16), int(hex(i), 16), (int(n, 16) * int(hex(i), 16))))

81
n = int(input())
for i in range(1, n+1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print("X", end=" ")
    else:
        print(i, end=" ")

82
r, g, b = map(int, input().split())
count = 0
for x in range(r):
    for y in range(g):
        for z in range(b):
            print("{} {} {}".format(x, y, z))
            count += 1
print(count)
83
h, b, c, s = map(int, input().split())
mb = round((h * b * c * s / 8) / 1024 / 1024, 1)
print('{} MB'.format(mb))
84
h, b, c = map(int, input().split())
mb = round((h * b * c / 8) / 1024 / 1024, 2)
print('{} MB'.format(mb))
85
h, b, c = map(int, input().split())
mb = round((h * b * c / 8) / 1024 / 1024, 2)
print('{:.2f} MB'.format(mb))

86
n = int(input())
sum = 0
for i in range(1, n+1):
    sum = sum+i
    i += 1
    if (sum >= n):
        break
print(sum)

87
n = int(input())
for i in range(1, n+1):
    if i % 3 == 0:
        continue
    print(i, end=" ")

88
a, d, n = map(int, input().split())
sum = a
for i in range(a, a+n-1):
    sum = sum+d
print(sum)

89
a, d, n = map(int, input().split())
sum = a
for i in range(a, a+n-1):
    sum *= d
print(sum)

90
a, m, d, n = map(int, input().split())
sum = a
for i in range(a, a+n-1):
    sum = sum*m+d
print(sum)
