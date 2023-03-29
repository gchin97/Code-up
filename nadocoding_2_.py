# input은 항상 문자열로 받음
# # temp = str(input())

# # for waiting_no in [0, 1, 2, 3, 4]:
# #     print("대기번호: {0}".format(waiting_no))


# # for waiting_no in range(5):
# #     print("대기번호: {0}".format(waiting_no))

# # starbucks = ["아이언맨", "토르", "아엠그루트"]

# # for customer in starbucks:
# #     print("{}, 커피가 준비되었어요".format(customer))

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다.{1}번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("종료되었습니다")


# customer = "토르"
# person = "unknown"
# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))


absent = [2, 5]
no_book = [7]
for i in range(1, 25):
    if i in absent:

print("{0}, 책 읽어".format(i))
