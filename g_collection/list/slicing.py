# 인덱스 슬라이싱
# animals = ['dog', 'dog', 'cat', 'bird', 'fish']

# list[inclusive_start=0 : exclusive_end=len(list)] -> list
# print(animals[0])
# print(animals[0:3])
# print(animals[1:4])
# print(animals[:2])
# print(animals[2:])

# list[inclusive_start=0 : exclusive_end=len(list) : step=1] -> list
# 메모리를 많이 소모하기 때문에 step은 사용을 지양한다.
# food = ['noodle', 'meat', 'bread', 'chicken']
# print(food[:3:2])
# print(food[2::2])

# 역순 출력
# print(food[::-1])

# number_list = list(range(1, 11))
#
# # [1, 3, 5, 7, 9]
# print(number_list[::2])
#
# # [6, 5, 4, 3, 2]
# print(number_list[5:0:-1])
#
# # [2, 4, 6] 2씩 증가하기 때문에 종료 인덱스가 6 또는 7 두가지가 가능하다.
# print(number_list[1:6:2])
# print(number_list[1:7:2])
#
# # [2, 3, 4, 5, 6, 7]
# print(number_list[1:7])

# animals = ['dog', 'dog', 'cat', 'bird']
# zoo = ['panda', 'giraffe']
#
# animals[1:2] = zoo
# print(animals)
#
# animals.insert(animals.index('dog') + 1, "giraffe")
# print(animals)
#
# animals.insert(animals.index('dog') + 1, zoo)
# print(animals)

# 슬라이싱, insert, del 를 사용하여 아래의 list 만들기
# ['dog', 'hamster', 'fish', 'dog' 'whale', 'bird']
animals = ['dog', 'dog', 'cat', 'bird']

del animals[animals.index('cat')]
# animals.remove('cat')
print(animals)

animals[-2: -3: -1] = ['whale']
print(animals)

animals.insert(animals.index('dog') + 1, 'fish')
print(animals)

animals.insert(animals.index('dog') + 1, 'hamster')
print(animals)

animals[1:3] = ['hamster', 'fish', 'dog']
print(animals)
