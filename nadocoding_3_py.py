scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, values in scores.items():
    # print(subject, values)
    print(subject.ljust(8), str(values).rjust(4), sep=":")

for num in range(1, 21):
    print("대기번호:", str(num).zfill(3))


print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
