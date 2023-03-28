1. set 을 사용하면 중복을 없애줌
s1 = ([1, 2, 3, 3, 4])
newList = list(set(s1))


a = [1, 2, 3]
이때 b는 a의 주소를 갖게 된 것임
b = a
하지만, 이건 a의 값을 갖게 된 것
b = a[:]

메모리의 새로운 주소에 새로운 값을 넣어라
b = copy(a)

a값과 b값을 바꾸기
a, b = b, a, a = b

for a in enumerate
for a in enumerate
for a in enumerate

t = 0
while t < 10:
    print("{0} 나무 넘어갑니다")
    t += 1
    if t == 10:
        print("나무 끝")
        break
