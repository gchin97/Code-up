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
            print("{},{},{}".format(x, y, z))
print(count)
83

84

85

86

87

88

89

90
