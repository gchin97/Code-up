from ..sound.echo import echo_test
from game.sound.echo import echo_test as e
from game.sound import *
from game.sound.echo import echo_test
from game.sound import echo
import game.sound.echo


def sum(a, b):
    result = a+b
    return result


print(sum(1, 2))

# 어떤 값이 아무리 많이 들어와도 다 넣고 싶을 땐, 몇개든 상관없이 다 들어감


def sum_many(*args):
    sum = 0
    return sum


print(sum_many(1, 2, 3))

# 딕셔너리형태로 여러개의 값을 들어오는 것을 처리하는 것, 특정 네임, value를 마음대로 받을 수 있는 것


def sum_many(**kargs):
    for k in kargs.key():
        if (k == "name"):
            print("당신의 이름은:"+kargs[k])


print(sum_many(name="int 조수", b="2"))

# return 값이 tuple 형태로 나옴


def sum_mul(a, b):
    return a+b, a*b, a-b


print(sum_mul(1, 2))
= > (3, 2, 1)

# 근데 난 여기서 더한 값만 쓸래 == 튜플에서 0번째만 뽑아옴


def sum_mul(a, b):
    return a+b, a*b, a-b


print(sum_mul(1, 2)[0])
= > (3, 2, 1)

# 함수를 축약모드로 다시 적기


def add(a, b):
    return a+b


def add(a, b): return a+b


# 예시
myList = [lambda a, b: a+b, lambda a, b: a*b]
# 람다 함수는 함수 안에서도 함수를 불러올 수 있음 마이리스트에서 첫번째꺼만 불러와~ 리스트 안에서 자체적으로 함수를 만들수 있는 좋은 기능
print(myList[0](1, 2))


# 파일 생성하기
f = open("new.txt", "w")
for i in range(1, 10):
    job = "%d번째 줄입니다.\n" % i
    f.write(job)
f.close()

# 한줄씩 읽어오기
f = open("new.txt", "r")
line = f.readline()
print(line)
f.close()

#  line= f.readlines 의 경우 리스트로 저장됨

f = open("new.txt", "r")
while True:
    line = f.readline()
    if not True:
        break
    print(line)
f.close()


#  line= f.read 의 경우 통째로 가져옴


# class
# 똑같은 함수를 여러번 쓰기 귀찮으니 클래스를 쓰게 됨
# class 의 이름은 항상 대문자!!!!

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

# New Class


class Fourcal():
    # init 이 있는 순간 Init 부터 해야됨
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result


a = Fourcal()
a.setdata(1, 2)
print(a.first)
print(a.second)

print(a.add())

# 부모 클래스를 사용해서 자식 클래스를 만들기


class MoreFourCal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result


a = MoreFourCal(4, 2)

# 모듈
__init__.py파일 에는 패키지 관련 설명을 할 수 있음

game.sound.echo.echo_test()

echo.echo_test()

echo_test()

e()

echo.echo_test()

# ..은 이전폴더로 들어가라는 뜻임


def render_test():
    print("render")
    echo_test()
