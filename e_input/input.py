# 문자열끼리만 연결(+)이 가능하다!
# data = 3
# print('안'+str(data))
# name = input("이름: ")
# mesage = '%s님 환영합니다.' % name
# print(mesage)
# print('{}님 환영합니다.'.format(name))
# print(f'{name}님 환영합니다.')

# 제 이름은 ???, 키는 ???cm입니다.
# 변수 선언
# 입력 함수로 이름과 키를 입력받고 변수에 저장
# name = input("이름: ")
# height = input("키: ")
# # format string을 통해 변수를 문자열에 적용하여 전체 문자열을 message 변수에 저장
# message = f'제 이름은 {name}, 키는 {height}cm입니다.'
# print(message)

# 두 정수를 입력 받은 후 곱셈 결과 출력
# number1 = int(input("첫번째 정수 입력: "))
# number2 = int(input("두번째 정수 입력: "))
# mul = number1 * number2
#
# message = f'{number1} x {number2} = {mul}'
# print(message)
# map함수는 여러개의 값을 한꺼번에 바꿀때 사용하는 함수
# input함수를 사용해서 전달받은 값을 split함수를 사용해서 ','를 기준으로 나눠준 후 입력값을 2개로 만들어 변수에 저장
# number1, number2 = map(int, input('두 정수를 입력하세요.\nex)1,3\n').split(','))
# print(number1 * number2)

# map(각각 어떻게 바꿀 것인가, [])
# 함수를 작성할 때 소괄호를 빼고 함수의 이름만 작성하면 함수의 주소값을 의미한다.
# message = '두 정수를 입력하세요.'
# example_message = '예)1, 3'
# number1, number2 = map(int, input(message + '\n' + example_message + '\n').split(', '))
# result = number1 * number2
# formatting = f'{number1} * {number2} = {result}'
#
# print(formatting)

# 현재 시간을 입력하고 시와 분으로 분리하여 출력
# message = '현재 시간을 입혁하세요\n'
# example_message = '예)11:30\n'
# hour, minute = map(int, input(message + example_message).split(':'))
# formatting = f'현재 시간은 {hour}시 {minute}분입니다.'
# print(formatting)

# 핸드폰 번호를 -(하이폰)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
# message = '본인의 전화번호를 입력하세요.\n'
# example_message = '예)010-1234-5678\n'
# first, second, third = input(message + example_message).split('-')
# formatting = f'당신의 전화번호는 {first}-{second}-{third}입니다.'
# print(formatting)

# 이름과 나이를 한 번에 입력받은 뒤 "000님의 나이는 000살" 형식으로 출력
# message = '본인의 이름과 나이를 입력하세요.\n'
# example_message = '예)홍길동, 30\n'
# name, age = input(message + example_message).split(', ')
# formatting = f'{name}님의 나이는 {age}살'
# print(formatting)

# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
message = '세개의 정수를 입력하세요.\n'
example_message = '예)1, 2, 3\n'
number1, number2, number3 = map(int, input(message + example_message).split(', '))
result = number1 + number2 + number3
formatting = f'입력하신 {number1}, {number2}, {number3}의 합은 {result}입니다.'
print(formatting)