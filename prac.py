# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i*j, end=" ")
#     print("")


result = [num*3 for num in range(1, 10) if num % 2 == 0]
print(result)

result = []
for x in range(2, 10):
    if num % 2 == 0:
        result.append(num*3)
