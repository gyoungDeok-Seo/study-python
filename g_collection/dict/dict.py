# student = {
#     "name": "서경덕",
#     "email": "kjkj0724@gmail.com"
# }
#
# print(student["name"])
# print(student.get("name"))
#
# # get()을 사용하면 key를 찾지 못했을 때 원하는 default 값으로 설정이 가능하며,
# # default 값이 없을 때에는 None을 가져온다.
# # print(student['phone']) # 오류
# print(student.get('phone', '01049124083'))
#
# # 'name' key 값이 이미 있기 때문에, 아래의 코드는 '수정'이다.
# student['name'] = '홍길동'
# print(student)
#
# # 'phone' ket 값이 없기 때문에, 아래의 코드는 '추가'이다.
# student['phone'] = '01049124083'
# print(student['phone'])
#
# if 'email' in student: # 수정
#     student['email'] = 'hgd1234@gmail.com'
# else: # 추가
#     student['email'] = 'hgd1234@gmail.com'
#
# print(student)

# my_dict = {
#     1: "서경덕",
#     "two": "20살",
#     "row": [
#         {"name": "ted", "age": 40},
#         {"name": "jack", "age": 30},
#         {"name": "john", "age": 20}
#     ]
# }
#
# # row에 있는 회원 3명의 정보를 모두 출력
# for i in my_dict["row"]:
#     print(i)
# print('====================')
# for i in my_dict:
#     if i == 'row':
#         for j in i:
#             print(j)
# print('====================')
# print(f'{my_dict["row"][0]["name"]}: {my_dict["row"][0]["age"]}')
# print(f'{my_dict["row"][1]["name"]}: {my_dict["row"][1]["age"]}')
# print(f'{my_dict["row"][2]["name"]}: {my_dict["row"][2]["age"]}')
# print('====================')
# print(my_dict.get("row"))
# print('====================')
#
# # 강사님 코드
# if 'row' in my_dict:
#     # print(type(my_dict["row"]))
#     for data in my_dict['row']:
#         print(f'{data["name"]}: {data["age"]}')

# 1~10까지 중 홀수와 짝수가 있다.
# 사용자가 '짝수'를 입력하면, 짝수만 출력하고
# '홀수'를 입력하면, 홀수만 출력한다.
# dict를 사용한다.
# numbers = {}
# print(numbers)
# for i in range(10):
#     number = i + 1
#     if number % 2 == 0:
#         numbers["짝수"] += number
#     else:
#         numbers["홀수"] += number
# print(numbers)

# numbers = {
#     "홀수": [i * 2 + 1 for i in range(5)],
#     "짝수": [(i + 1) * 2 for i in range(5)]
# }

# numbers = {
#     True: [i * 2 + 1 for i in range(5)],
#     False: [(i + 1) * 2 for i in range(5)]
# }
#
# message = '홀수와 짝수 중 하나를 입력하세요: '
# choice = input(message)
# print(numbers.get(choice))
# print(", ".join(map(str, numbers.get(choice) == '홀수')))

student = {
    "name": "서경덕",
    "email": "kjkj0724@gmail.com"
}

# key 분리
print(list(student.keys()))

# value 분리
print(list(student.values()))

# item 분리
print(list(student.items()))
for key, values in student.items():
    print(key, values)