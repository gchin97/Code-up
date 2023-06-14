# 1. set 을 사용하면 중복을 없애줌
# s1 = ([1, 2, 3, 3, 4])
# newList = list(set(s1))


# a = [1, 2, 3]
# 이때 b는 a의 주소를 갖게 된 것임
# b = a
# 하지만, 이건 a의 값을 갖게 된 것
# b = a[:]

# 메모리의 새로운 주소에 새로운 값을 넣어라
# b = copy(a)

# a값과 b값을 바꾸기
# a, b = b, a, a = b

# for a in enumerate
# for a in enumerate
# for a in enumerate

# t = 0
# while t < 10:
#     print("{0} 나무 넘어갑니다")
#     t += 1
#     if t == 10:
#         print("나무 끝")
#         breakㅁ

numpy 
1. 다차원 배열 생성 방법
- np.array(리스트), np.array(중첩 ㅣ스트)
- np.zeros, np.ones, np.empty, np.full
- 랜덤 함수 이용하기(np.random.함수)
- np.linspace
2. 속성
- ndim(차원 정보)
- shape(모양 볼 수 있음)
- dtype(data type, 정수 np.int32, 실수 np.float64, 문자열 np.string/str
3. 추가 삽입 색인
- np. append, np. insert, np.delete
4. 색인
- indexing (순방향, 역방향)
- 슬라이싱(np.s_[:])
- fancy 색인: 정수형 배열 색인 => 변수[[idx, idx]]

x = [1,2,3]
x2 = x #얕은 복사(주소값 복사), 따라서 x2에서 값을 변경하면 x 도 변경이 됨 
x1 = x2 함수를 사용하지 않고 주소를 복사해서 넌 너고 난 나야 x2 변경했을때 x1도 변경됨 

- python의 깊은 복사 3가지 방법 (깊은 복사이기 때문에 x3에서 값을 변경해도 원본인 x는 영향받지 않음)
x3 = x[:]
x3 = x.copy(x)
x3 = list(x) 

- numpy는 [:] 슬라이싱  처리는 얕은 복사로 처리

- [:]
        [:[
          
          
