from random import *
print(random())  # this is a random float number from 0 to 1
print(int(random()*10))  # this is random int number from 0 to 9
print(int(random()*10)+1)  # this is random int number from 0 to 10
print(randrange(1, 11))  # this is random int number from 0 to 10
print(randint(1, 10))

r = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월", str(r), "일로 선정되었습니다.")

python = 'Python is amazing'
print(python.upper())
print(python.lower())
print(python[0].isupper())
print(len(python))
print(python.replace("python", "Java"))
index = python.index("n")

index = python.index("n", index+1)
print(python.find("Python"))
print(index)

# d 는 정수값!!!!!!!!!!!
print("나는 %d 살입니다." % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple 은 %c로 시작해요" % "A")  # 한글자만 받을게요

# 뭐든 %s로 바꿔도 ㄱㅊ %s 는 치트키임 ㅋㅋ
print("나는 %s값과 %s값을 좋아해요" % ("파란", 3))

print("나는 {}살입니다." .format(20))
print("나는 {}값과 {}값을 좋아해요" .format("파란", 3))
print("나는 {1}값과 {0}값을 좋아해요" .format("파란", 3))  # 중괄호 안에 숫자를 넣으면 입력대로 나옴
print("나는 {age}값과 {color}값을 좋아해요" .format(
    color="파란", age=3))  # 중괄호 안에 숫자를 넣으면 입력대로 나옴
age = 20
color = 'blue'
print(f"나는 {age}값과 {color}값을 좋아해요")

# \\ -> 문장내에서 \로 바뀜
url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e"))+"!"
print("{0} password is {1}".format(url, password))
