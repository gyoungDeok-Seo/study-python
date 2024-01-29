user_info = [
    {'number': 1, 'name': 'john'},
    {'number': 2, 'name': 'mike'},
    {'number': 3, 'name': 'ted'},
    {'number': 4, 'name': 'lindy'},
    {'number': 5, 'name': 'adam'},
]

# number = 5
#
# # 추가
# # 회원 번호는 자동 증가한다.
# def insert(name):
#     user_number = user_info[-1]['number'] + 1
#     user_info.append({'number': user_number, 'name': name})
#
# # 목록
# def user_list():
#     '''
#     목록을 출력하는 함수
#     '''
#
#     for i in range(len(user_info)):
#         print(user_info[i])
#
#
# # 조회(번호로 조회)
# def user_search(number):
#     '''
#     회원번호로 회원 조회
#     :param number: 회원 번호
#     '''
#     result = None
#     for i in range(len(user_info)):
#         if user_info[i]['number'] == number:
#             result = user_info[i]
#     print(result)
#
#
# user_search(8)
# print('=====수정=====')
# # 수정(번호로 이름 수정)
# def user_info_modify(*, number, name):
#     global user_info
#     for i in range(len(user_info)):
#         if user_info[i]['number'] == number:
#             user_info[i]['name'] = name
#
# # 삭제(번호로 삭제)
# def user_delete(number):
#     for i in range(len(user_info)):
#         if user_info[i]['number'] == number:
#             del user_info[i]
#             break

# post_info = [
#     {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
#     {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
#     {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
#     {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
#     {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
# ]
# # 전역 변수
# number = 5
#
# # 추가(조회수는 전달받지 않고 기본값 0으로 설정)
# def insert(*, title, content, file, read_count=0):
#     global number
#     number += 1
#     post_info.append({'number': number, 'title': title, 'content': content, 'file': file, 'read_count': read_count})
#
#
# print('=====목록=====')
# # 목록(최신순으로 조회)
# def select_all():
#     return post_info[::-1]
#
#
# print(select_all())
# print('=====조회=====')
# # 조회(번호로 조회, 조회수 1 증가)
# def select(number, read=0):
#     '''
#     :param number: 게시글 번호
#     :param read: 게시글의 보는지 특정하는지 유무
#     :return: 게시글
#     '''
#     for post in post_info:
#         if post['number'] == number:
#             if read:
#                 post['read_count'] += 1
#             return post
#
#
# print(select(5, 1))
# print(select_all())
# print('=====수정=====')
# # 수정(번호로 정보 수정)
# def update(**kwargs):
#     '''
#
#     :param kwargs: {'number': 게시글 번호, 'title': 수정할 제목, 'content': 수정할 내용, 'file': 수정할 파일}
#     '''
#     post = select(kwargs['number'])
#     post['title'] = kwargs['title']
#     post['content'] = kwargs['content']
#     post['file'] = kwargs['file']
#
#
# print(select(5, 1))
# update(number=5, title='예제 제목5', content= '예제 내용5', file='더미주소5')
# print(select(5))
# print('=====삭제=====')
# # 삭제(번호로 삭제)
# def delete(number):
#     del post_info[post_info.index(select(number))]
#
#
# delete(5)
# print(select(5))
#