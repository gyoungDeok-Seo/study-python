# 1 ~ 15까지 출력
# for i in range(15):
#     print(f'{i + 1}', end=' ')
# print()

# 30 ~ 1까지 출력
# for i in range(30):
#     print(f'{30 - i}', end=' ')
# print()

# 1 ~ 100까지 중 홀수만 출력
# for i in range(50):
#     condition = i * 2 + 1
#     print(condition, end=' ')
# print()

# 1 ~ 10까지 합 출력
# result = 0
# for i in range(10):
#     number = i + 1
#     result += number
# print(result)

# 1 ~ n까지 합 출력
# message = '정수: '
# n = int(input(message))
# result = 0
#
# for i in range(n):
#     number = i + 1
#     result += number
# print(result)

# 3 4 5 6 3 4 5 6 3 4 5 6 출력
# for i in range(12):
#     result = i % 4 + 3
#     print(result, end=' ')
# print()

# '1,235,500'를 1235500으로 출력
# result = ''
# for i in '1,235,500'.split(','):
#     result += i
#
# print(result)

# 강사님 코드
# data = '1,235,500'
# result = ''
# for i in data:
#     if i != ',':
#         result += i
#
# result = int(result)
# print(result + 5)

# 입력 받은 값으로 구구단 만들기
# ex) 입력 받은 값: 3
# 3단
# 3 X 1 = 3
# 3 X 2 = 6
# ...
# 3 X 9 = 27

message = '정수 입력: '
number1 = int(input(message))

for i in range(10):
    if i == 0:
        print(f'{number1}단')
        continue
    number2 = i + 1
    mul = number1 * number2
    result = f'{number1} X {number2} = {mul}'

    print(result)
