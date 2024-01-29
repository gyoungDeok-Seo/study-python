# 'aPPle', 'BananA', 'meLON'을 모두 소문자로 변경
messages = ['aPPle', 'BananA', 'meLON']
change = list(map(lambda message: message.lower(), messages))
print(change)

# 입력받은 한글을 정수로 변경
# 입력 예: 삼오일구
# 출력 예: 3519
examples = input('숫자를 한글로 입력하세요.\n')
hanglul = '공일이삼사오육칠팔구'

result = int("".join(list(map(lambda example: str(hanglul.index(example)), examples))))
print(result)
# 입력받은 정수를 한글로 변경
# 입력 예: 3519
# 출력 예: 삼오일구
examples = input('숫자를 입력하세요.\n')
hanglul = '공일이삼사오육칠팔구'

result = "".join(list(map(lambda example: hanglul[int(example)], examples)))
print(result)


# 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'

# 위 경로 중 회원 서비스가 아닌 경로만 추출
# 1. 서비스명(user, post, order)으로 변경(map)
# 2. 서비스명 중 'user'가 아닌 경로만 추출(filter)
urls = ['user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read']

changes = list(map(lambda url: url.split('/')[0], urls))
print(changes)

result = list(filter(lambda change: change != 'user',changes))
print(result)

# 강사님 코드
# 'aPPle', 'BananA', 'meLON'을 모두 소문자로 변경
fruits = ['aPPle', 'BananA', 'meLON']
result = list(map(lambda fruit: fruit.lower(), fruits))
print(result)

# 입력받은 한글을 정수로 변경
# 입력 예: 삼오일구
# 출력 예: 3519
hangul = "공일이삼사오육칠팔구"
data = "삼오일구"

print(int("".join(list(map(lambda s: str(hangul.index(s)), data)))))


# 입력받은 정수를 한글로 변경
# 입력 예: 3519
# 출력 예: 삼오일구
hangul = "공일이삼사오육칠팔구"
data = 3519
print("".join(list(map(lambda s: hangul[int(s)], str(data)))))
# print("".join(list(map(lambda s: hangul[ord(s) - 48], str(data)))))

# 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'
# 위 경로 중 회원 서비스가 아닌 경로만 추출
# 1. 서비스명(user, post, order)으로 변경(map)
# 2. 서비스명 중 'user'가 아닌 경로만 추출(filter)
# 출력 예시
# ['post', 'order', 'order', 'post']
urls = ['user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read']

print(list(filter(lambda service: service != 'user', list(map(lambda url: url[:url.index("/")], urls)))))