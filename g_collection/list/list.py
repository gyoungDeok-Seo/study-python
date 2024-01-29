# # animals = ["dog", "cat", "bird", "fish"]
# #
# # print(animals)
# # print(type(animals))
# #
# # # 인덱스로 접근
# # print(animals[1])
# # print(animals[2])
# #
# # # 음수 인덱스 가능(가장 마지막부터 순서대로 앞으로 이동한다)
# # print(animals[-1])
# # print(animals[-2])
# #
# # # len()
# # print(len(animals))
# #
# # # append()
# # animals.append("hamster")
# # print(len(animals))
# # print(animals)
# #
# # animals.append("cat")
# # print(animals)
# #
# # # insert()
# # animals.insert(1, "dog")
# # print(animals)
# #
# # # remove()
# # animals.remove("fish")
# # print(animals)
# #
# # # del()
# # # del(animals[1])
# # del animals[1]
# # print(animals)
# #
# # # claer()
# # # animals.clear()
# # # print(animals)
# #
# # # index()
# # print(animals.index("bird"))
# # # print(animals.index('tiger'))
# #
# # # 수정
# # index = animals.index('bird')
# # animals[index] = 'lion'
# # print(animals)
# #
# # # 그 외
# # animals = ["dog", "cat", "bird", "fish"]
# # print(animals * 2)
# #
# # print("dog" in animals)
# # print("tiger" in animals)
# # for animal in animals:
# #     print(animal)
#
# # 실습
# # 1~90까지 list에 담고 출력
# # ninety = list(range(1,91))
# # print(ninety)
#
# ninety = [0] * 90
# for i in range(len(ninety)):
#     ninety[i] = i + 1
# print(ninety)
# # 1~100까지 중 짝수만 list에 담고 출력
# even = [0] * 50
# for i in range(len(even)):
#     even[i] = i * 2 + 2
#     # even.append(i * 2 + 2)
#     # even.insert(i, i * 2 + 2)
# print(even)
#
# # 1~10까지 list에 담은 후 짝수만 출력
# even = list(range(1,11))
# print(even)
# for i in even:
#     if i % 2 == 0:
#         print(i)
#
# # 4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
# member = ['홍길동', '이순신', '나혜석', '유관순']
# print(member) # 선언된 list 확인을 위해 출력
#
# member[1] = '세종대왕' # 두번째 회원의 이름 변경
# print(member) # 변경 확인을 위해 출력
#
# del member[-1] # 마이너스 인덱스를 사용하여 마지막 회원 삭제
# print(member) # 변경 확인을 위해 출력
#
# # "189,000 원" 을 189000으로 변경, 제너레이터 사용

# list안에 list
number_list = [[1, 3, 5],[2, 4, 6]]
for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])