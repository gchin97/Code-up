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
