# list 의 경우 pop 가능
from random import *
num_list = [5, 4, 3, 6, 1]
mix_list = ['조세호', 3]
print(num_list)
num_list.extend(mix_list)
print(num_list)

cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet.get(3))
print(cabinet.get(5, "사용 가능"))

cabinet["5"] = "정형돈"
print(cabinet)
del cabinet["5"]
print(cabinet)

# 한번에 변수를 넣어둘 수 있음
name, age, hobby = "김종국", 20, "코딩"
print(name, age, hobby)

# set 는 중복 안되고 순서가 없음
my_set = {1, 2, 3, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "정형돈"}
python = set(["유재석", "양세형"])
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

menu = {"a", "b", "c"}
menu = list(menu)
menu = tuple(menu)
print(menu, type(menu))
menu = set(menu)  # 다시 세트로 바꿀 수 있음


students = list(range(1, 21))

winners = sample(students, 4)
# coffee = sample(randint(students), 3)
print("-- 당첨자 발표--")
print("치킨 당첨자 : {}" .format(winners[0]))
print("커피 당첨자 : {}" .format(winners[1:]))

print

# shuffle(list)
# print(sample(list, 1))
