# fish.txt
# 사용자에게 입력받은 물고기를 fish.txt에 작성한다.
# 사용자가 q를 입력하면 fish.txt의 전체 내용을 삭제한다.
# 사용자가 r를 입력하면 fish.txt의 전체 내용을 콘솔에 출력한다.
# fish = input('물고기: ')
# if fish == 'q':
#     with open('fish.txt', 'w', encoding='utf-8') as file:
#         file.write('')
#
# elif fish == 'r':
#     with open('fish.txt', 'r', encoding='utf-8') as file:
#         for line in file.readlines():
#             print(line, end='')
#         # while file.readline() != '':
#         #     file.readline()
#         #     print(file.readline(), end='')
#
# else:
#     with open('fish.txt', 'a', encoding='utf-8') as file:
#         file.write(f'{fish}\n')

# fish.txt
# 사용자에게 입력받은 물고기를 fish.txt에 작성한다.
# 사용자가 q를 입력하면, fish.txt의 전체 내용을 삭제한다.
# 사용자가 r을 입력하면, fish.txt의 전체 내용을 콘솔에 출력한다.

# with open('./fish.txt', 'w', encoding='utf-8') as file:
#     pass

# with open('./fish.txt', 'a', encoding='utf-8') as file:
#     fish = input('물고기: ') + '\n'
#     file.write(fish)

# with open('./fish.txt', 'r', encoding='utf-8') as file:
#     for line in file.readlines():
#         print(line, end='')

# title = 'q: 삭제, r: 읽기'
# message = '물고기: '
#
# while True:
#     path = input('경로: ')
#     fish = input(title + '\n' + message)
#
#     if fish == 'q':
#         with open(path, 'w', encoding='utf-8') as file:
#             pass
#
#     elif fish == 'r':
#         try:
#             with open(path, 'r', encoding='utf-8') as file:
#                 for line in file.readlines():
#                     print(line, end='')
#             break
#         except FileNotFoundError:
#             print('경로를 다시 확인해주세요.')
#
#     else:
#         with open(path, 'a', encoding='utf-8') as file:
#             file.write(fish + '\n')

# 고등어를 참치로 수정하기
content = ''
with open('fish.txt', 'r', encoding='utf-8') as file:
    line = None
    while line != '':
        line = file.readline()
        if line == '고등어\n':
            content += '참치\n'
            continue
        content += line

    print(content)

with open('fish.txt', 'w', encoding='utf-8') as file:
    file.write(content)

with open('fish.txt', 'r', encoding='utf-8') as file:
    print("".join(file.readlines()))