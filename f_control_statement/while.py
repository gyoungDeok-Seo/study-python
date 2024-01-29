# 사용자가 입력한 정수가 몇 자리수인지 출력
# 1. 사용자에게 정수를 입력받는다.
# 2. 입력받은 정수의 각 자리수를 센다.
# 3. 자리수를 출력한다.
# 힌트: 몫
# number = int(input('정수 입력:'))
#
# count = 0
# while number != 0:
#     number //= 10
#     count += 1
#
# print(count)

# while문 예제
# 비밀번호를 입력받고 같은지 파악 후 경우에 따른 메시지를 뛰워주세요.
# 비밀번호가 틀릴 경우 다시 입력하도록 하세요. 메시지 출력 후 다시 입력 받아야합니다.
# 일치할 경우 '로그인 성공' 메시지를 출력하세요.

password = '1234'
input_password = input('비밀번호: ')

while input_password != password:
    print('비밀번호가 일치하지 않습니다.')
    input_password = input('비밀번호: ')
print('로그인 성공')