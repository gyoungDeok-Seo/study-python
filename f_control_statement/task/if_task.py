#사용자에게 아래의 메뉴를 출력하고 번호를 입력받는다.

# 1. 빨간색
# 2. 검은색
# 3. 노란색
# 4. 흰색

# 사용자가 입력한 번호의 색상을 영어로 출력한다.
# message = '예시의 4가지 색상 중 하나의 번호를 입력하세요.\n'
# example_message = '예) 1. 빨간색\n2. 검은색\n3. 노란색\n4. 흰색\n'
# use_select = int(input(message + example_message))
#
# if use_select == 1:
#     color = 'red'
# elif use_select == 2:
#     color = 'black'
# elif use_select == 3:
#     color = 'yellow'
# else:
#     color = 'white'
# print(color)

# 강사님 코드
# title = "색상은 골라주세요!\n"
# menu = "1. 빨간색\n" \
#        "2. 검은색\n" \
#        "3. 노란색\n" \
#        "4. 흰색\n"
#
# choice = int(input(title + menu))
# choice1, choice2, choice3, choice4 = choice == 1, choice == 2, choice == 3, choice == 4
# color1, color2, color3, color4 = "red", "black", "yellow", "white"
# result = None
#
# if choice1:
#     result = color1
# elif choice2:
#     result = color2
# elif choice3:
#     result = color3
# elif choice4:
#     result = color4
#
# print(result)

# 입력받은 만 나이를 기준으로 연령대 구분하기
# 영유아 0~5 infants
# 아동 6~12 child
# 청소년 13~18 teenager
# 청년 19~29 youth
# 중년 30~49 middle age
# 장년 50~64 prime_of_life
# 노년 65 old_age

message = '나이: '
age = int(input(message))

infants_condition = 0 <= age < 6
child_condition = 6 <= age < 13
teenager_condition = 13 <= age < 19
youth_condition = 19 <= age < 30
middle_age_condition = 30 <= age < 50
prime_of_life_condition = 50 <= age < 64

if infants_condition:
    age_group = '영유아'
elif child_condition:
    age_group = '아동'
elif teenager_condition:
    age_group = '청소년'
elif youth_condition:
    age_group = '청년'
elif middle_age_condition:
    age_group = '중년'
elif prime_of_life_condition:
    age_group = '장년'
else:
    age_group = '노년'

print(f'당신의 나이는 {age}세로 {age_group}입니다.')