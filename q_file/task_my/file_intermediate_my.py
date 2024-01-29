# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""
# 실습 시간 동안 작성한 코드
# with open('alice.txt', 'r', encoding='utf-8') as file:
#     read_split_words = file.read().split(' ')
#     isalpha_words = []
#     # print(words)
#     # print(len(words))
#     print(type(file.read()))
#     sentence = file.read()
#     print(words)
#     for i in range(len(read_split_words)):
#         # print(read_split_words[i], read_split_words[i].isalpha())
#         if read_split_words[i].isalpha():
#             isalpha_words.append(read_split_words[i].lower())
#
#         else:
#             if '`' in read_split_words[i]:
#                 pass
#             elif read_split_words[i].isdecimal():
#                 pass
#             else:
#                 continue

# 현재 경로의 alice.txt 파일을 가져와 읽고 utf-8로 인코딩한 후 file에 주소 값을 담는다.
# open 함수만 사용하게 되면 따로 close 함수를 사용해야 하지만 with은 따로 사용하지 않아도 된다.
# 또한 with을 사용할 경우 영역안에서 open한 파일의 주소값을 객채에 담아 사용할 수 있다.
with open('alice.txt', 'r', encoding='utf-8') as file:
    # 불러온 파일의 내용을 str형태로 가져오는 read메소드를 사용하고
    # 소대문자 구분없이 비교하기 위해 lowr메소드를 사용해서 모든 영어 문자를 소문자로 바꾸어 words에 저장
    content = file.read().lower()
# print(words) # 변형된 값을 보기위해 출력해 봤다.

temp = ""
# words의 문자열안의 문자들을 하나식 가져온다.
for character in content:
    # 알파벳 문자열끼리 비교연산자를 사용하면 아스키 코드 값으로 비교하기 때문에
    # 만약 character가 a ~ z라면,
    if 'a' <= character <= 'z':
        # temp에 character를 연결
        temp += character

    # character가 a ~ z에 포함되지 않는다면
    else:
        # temp에 공백 연결(단어 구분 시 구분점으로 사용하기 위해)
        temp += " "
# print(temp) # 문제없이 연결되었는지 확인하기 위해 사용

# 문자열 중 공백을 구분점으로 하여 각 단어들을 index에 list로 저장
words = temp.split()
# print(words)

# words 안에 값들을 인덱스 순차적으로 가져와 길이가 1을 초과하는 값만 리스트에 담고 저장
filtered_words = [
    word
    for word in words
    if len(word) > 1
]
# print(filtered_words) # 문제없이 담겼는지 확인하기 위해 사용

result = {}
# filtered_words 안에 값들을 순차적으로 가져와 word에 담는다.
for word in filtered_words:

    # 만약 result안에 키값으로 word가 사용되고 있지 않다면
    if word not in result:
        # result에 word를 키값으로 1을 저장
        result[word] = 1

    # 만약 result안에 키값으로 word가 사용되고 있다면
    else:
        # value 값 1 증가시키고 저장
        result[word] += 1
# print(result) # 단어와 개수가 제대로 저장 되었는지 확인하기 위해 사용

# result dict에서 key값들을 가져와 value 값이 100 이상인 값들을
# set에 word: result[word] 형태로 담고 dict로 만들어 저장
result = {
    word: result[word]
    for word in result
    if result[word] >= 100
}
# print(result) # 코드에 문제가 없는지 확인하기 위해 사용

# sorted함수를 사용해서 result 안에 각각의 key를 get함수에 전달해여
# value를 기준으로 key를 내림차순으로 정렬하고 저장
sorted_key = sorted(result, key=result.get, reverse=True)
# print(sorted_key) # key 값으로 저장되었는지 보기위해 사용

# key 순차적으로 가져와 key왜 result의 value를 출력
for key in sorted_key:
    print(key, result[key])
















