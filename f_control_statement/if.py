# number = 15

# 나머지연산자 모듈러스라고도 한다. mod로 쓰는 언어도 있다
# if number % 3 == 0:
#     print(f"{number}는 3의 배수입니다.")
# if number % 5 == 0:
#     print(f"{number}는 5의 배수입니다.")

# number가 양수인지, 음수인지, 0인지 검사
# number = 0
#
# if number > 0:
#     formatting = f"{number}은/는 양수입니다."
# elif number != 0:
#     formatting = f"{number}은/는 음수입니다."
# else:
#     formatting = f"{number}은/는 0입니다."
# print(formatting)

# 강사님 코드
# number = 0
#
# positive_condition = number > 0
# negative_condition = number < 0
#
# if positive_condition:
#     formatting = f"{number}은/는 양수입니다."
# elif negative_condition:
#     formatting = f"{number}은/는 음수입니다."
# else:
#     formatting = f"{number}"
# print(formatting)

# 나이를 입력받은 후 미성년자인지 검사
# message = '만 나이: '
# age = int(input(message))
# id_check = age < 20
#
# if id_check:
#     print("미성년자입니다.")
# else:
#     print('성인입니다.')

# message = '나이: '
# age = int(input(message))
# condition = 0 < age < 20
# error_condition = age <= 0
#
# if condition:
#     print('미성년자입니다.')
# elif error_condition:
#     print('잘못 입력하셨습니다.')
# else:
#     print('성인입니다.')

# 두 정수를 입력받은 후 대소비교 진행
message = '두 정수를 입력하세요.\n'
example_message = '예)20 49\n'
number1, number2 = map(int, input(message + example_message).split())
# 초기화 - 선언할 때 넣을 값을 모를 경우 초기값을 넣어준다.
# 사용할 자료형을 알려줄 수 있다.
# 정수: 0
# 실수: 0.0
# 문자열: '' 또는 ""
# 불린: False

formatting = ''

condition1 = number1 > number2
condition2 = number1 < number2

# 일괄처리란,
# 각 분기별로 결과를 처리하지 않고
# 모든 분기 종료 후 한번에 처리하는 것을 의미한다.

if condition1:
    formatting = f'{number1}이/가 {number2}보다 큽니다.'
elif condition2:
    formatting = f'{number1}이/가 {number2}보다 작습니다.'
else:
    formatting = '두 수가 같습니다.'

print(formatting)
