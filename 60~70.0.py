60
a, b = map(int, input().split())
print(int(a | b))

61
a, b = map(int, input().split())
print(int(a ^ b))

62
a, b = map(int, input().split())
print(a if a > b else b)

63
a, b = map(int, input().split())
print(a if a > b else b)

64
a, b, c = map(int, input().split())
print((a if a < b else b) if (a if a < b else b) < c else c)

65
data = input().split()
for i in data:
    if (int(i) % 2 == 0):
        print(int(i))
65
i = int(input())
if (i > 0 and i % 2 == 0):
    print("C")
elif (i > 0 and i % 2 == 1):
    print("D")
elif (i < 0 and i % 2 == 0):
    print("A")
elif (i < 0 and i % 2 == 1):
    print("B")
67
i = int(input())
if (i > 0 and i % 2 == 0):
    print("C")
elif (i > 0 and i % 2 == 1):
    print("D")
elif (i < 0 and i % 2 == 0):
    print("A")
elif (i < 0 and i % 2 == 1):
    print("B")

68
i = int(input())
if 90 <= i <= 100:
    print("A")
elif 70 <= i <= 89:
    print("B")
elif 40 <= i <= 69:
    print("C")
elif 0 <= i <= 39:
    print("D")

69
i = input()
if i == "A":
    print("best!!!")
elif i == "B":
    print("good!!")
elif i == "C":
    print("run!")
elif i == "D":
    print("slowly~")
else:
    print("what?")

70
i = int(input())
if i//3 == 1:
    print("spring")
elif i//3 == 2:
    print("summer")
elif i//3 == 3:
    print("fall")
elif i//3 >=4 or i//3 == 0:
    print("winter")
