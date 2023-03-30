# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, values in scores.items():
#     # print(subject, values)
#     print(subject.ljust(8), str(values).rjust(4), sep=":")

# for num in range(1, 21):
#     print("대기번호:", str(num).zfill(3))


# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))


# for i in range(1, 5):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write(" - {}주차 주간보고".format(i))
#         report_file.write("\n부서:")
#         report_file.write("\n이름:")
#         report_file.write("\n업무 요약:")

class Unit:
    # 셀프를 제외한 개수만큼 아래 호출할 때 객체를 만들어야 함
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성되었습니다.".format(self.name))
        print("hp는 {}이고, 공격력 {}입니다.".format(self.hp, self.damage))

# # instance of Unit
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 5)

# Class

# 공격 유닛 
class AttackUnit: 
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attach(self, location):
        print("{0}:{1} 방향으로 적군ㅇ르 공격합니다. 공격력 {2}".format(self.name, location, self.damage))
    
    def damage(self, damage):
        print("{0}: {1} is damaged".format(self.name, damage))
        self.hp-= damage
        if self.hp<=0:
            print("파괴되었습니다.")
    
    def 