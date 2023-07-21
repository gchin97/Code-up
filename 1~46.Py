aaaj
a/maaas1/a
print("hello")
2
print("Hello World")
3123
print("Hello\n World")a
4
print("'Hello'")asdf
5
print('"Hello World"')
6
print("\"!@#$%^&*()\'")
7
print("\"C:\Download\\'hello'.py\"")
8
print('print("Hello\\nWorld")')
9
print(input())
10
print(int(input()))
11
print(float(input()))

12
a = int(input())
b = int(input())
print(a)
print(b)

13
a = input()
b = input()
print(a)
print(b)

14
a = float(input())
for i in range(3):
    print(a)

15
a, b = input().split()
print("{}\n{}".format(a, b))

16
a, b = input().split()
print("{0} {1}".format(b, a))

17
s = input()
print("{0},{0},{0}".format(s))

18
a, b = input().split(":")
print(a, b, sep=":")
19
a, b, c = input().split("-")
print(c, b, a, sep="-")
20
a, b = input().split("-")
print("{}{}".format(a, b))

21

a = input()
for i in a:
    print(i)

22

a = input()
YMD = a[:2]
Month = a[2:4]
day = a[4:]

print(Y, M, D)

23
Y, M, D = input().split(":")
print(M)

24
a, b = input().split()
print(a+b)

25
a, b = map(int, input().split())
print(a+b)

26
num1 = input()
num2 = input()

result = float(num1) + float(num2)
print(result)

27
a = int(input())
print("%x" % a)

28
a = int(input())
print("%X" % a)

29
a = input()
b = int(a, 16)
print("%o" % b)

30
a = input()
b = ord(a)
print(b)

31
a = int(input())
print(chr(a))

32
a = ord(input())
print(chr(a+1))

34
a, b = map(int, input().split())
c = a-b
print(c)
35
a, b = map(float, input().split())
c = a*b
print(c)

36
a, b = input().split()
c = int(a)*b
print(c)

37
a = int(input())
b = str(input())
c = a*b
print(c)
38

a, b = map(int, input().split())
c = a**b
print(c)

39

a, b = map(float, input().split())
c = a**b
print(c)
40

a, b = map(int, input().split())
c = a//b
print(c)

40
a, b = map(int, input().split())
c = a//b
print(c)

41
a, b = map(int, input().split())
c = a % b
print(c)

42
a, b = map(float, input().split())
print("%.3f" % round((a/b), 3))

43
a, b = input().split()
a = int(a)
b = int(b)
if (a >= 0 and b != 0):
    print(a+b)
    print(a-b)
    print(a*b)
    print(int(a/b))
    print(a % b)
    print(format(a/b, ".2f"))

45
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
sum = a+b+c
A = (a+b+c)/3
print(sum, format(A, ".2f"))

46
a = int(input())

print(a << 1)

47
a, b = map(int, input().split)
a = int(a)
b = int(b)
if 0 < a <= 10 and 0 <= b <= 10:
    print(a*(2**b))
    print(a)
