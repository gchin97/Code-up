1
print("hello")
2
print("Hello World")
3
print("Hello\n World")
4
print("'Hello'")
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
