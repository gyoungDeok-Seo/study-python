# 회원 정보 실습
# user_info = [
#     {'number': 1, 'name': 'john'},
#     {'number': 2, 'name': 'mike'},
#     {'number': 3, 'name': 'ted'},
#     {'number': 4, 'name': 'lindy'},
#     {'number': 5, 'name': 'adam'},
# ]
# # 전역 변수
# number = 5
#
#
# # 추가
# # 회원 번호는 자동 증가한다.
# def insert(name):
#     """
#     전달 받은 name 값과 자동 증가하는 number 값을 user_info에 dict로 추가하는 함수
#     :param name: 추가할 이름
#     """
#     # 전역 변수를 수정하기 위해 선언
#     global number
#     # 함수가 실행 될때마다 전역 변수 number 증가 후 저장
#     number += 1
#     # user_info list에 append를 통해 number와 name을 value값으로 담은 새로운 dict 값을 추가
#     user_info.append({'number': number, 'name': name})
#
#
# # 목록
# def select_all():
#     """
#     회원 전체 목록을 return하는 함수
#     :return: 회원 전체 목록
#     """
#     return user_info
#
#
# # 조회(번호로 조회)
# def select_by_number(number):
#     """
#     전달받은 number로 해당되는 회원을 검색하는 함수
#     :param number: 검색할 회원의 번호
#     :return: 검색된 회원 정보(dict)
#     """
#     # user_info안의 값들로 사용하기 위해  반복 진행
#     for user in user_info:
#         # user에 'number' key 값을 사용하는 value 중 매개변수인 number와 같다면
#         if user['number'] == number:
#             # 해당 user 정보 return
#             return user
#
#
# # 수정(번호로 이름 수정)
# def update(**kwargs):
#     """
#     
#     :param kwargs:
#     :return:
#     """
#     #
#     target = select_by_number(kwargs['number'])
#     #
#     target['name'] = kwargs['name']
#
#
# # 삭제(번호로 삭제)
# def delete(number):
#     """
#
#     :param number:
#     :return:
#     """
#     #
#     #
#     #
#     del user_info[user_info.index(select_by_number(number))]
#
# print(select_all())
# insert('seo')
# print(select_all())
# print(select_by_number(3))
# update(number=5, name='deok')
# print(select_by_number(5))
# print(select_all())
# delete(2)
# print(select_all())


# 게시글 정보 실습
post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]

# 전역 변수
number = 5


# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
def insert(title, content, file, read_count=0):
    """
    매개변수들을 통해 post를 추가하는 함수
    :param title: 게시글 제목
    :param content: 게시글 내용
    :param file: 첨부파일 경로
    :param read_count: 조회수(기본값 0 입력금지)
    """
    # 각 'title', 'content', 'file', 'read_count'를 key 값으로 하고 같은 이름의 매개변수를 value값으로 하는
    # 하나의 dict를 post_info list에 append한다.
    post_info.append({'title': title, 'content': content, 'file': file, 'read_count': read_count})


# 목록(최신순으로 조회)
def select_all():
    """
    post_info를 역순으로 slicing 해서 return 하는 함수
    :return: post_info[::-1]
    """
    return post_info[::-1]


# 조회(번호로 조회, 조회수 1 증가)
def read(number):
    """
    select 함수를 사용하여 검색된 post의 'read_count'를 증가시키는 함수
    :param number: 조회수를 증가시킬 게시글 번호
    """
    post = select(number)
    post['read_count'] += 1


def select(number):
    """
    전달받은 매개변수로 해당하는 게시글을 검색해서 return하는 함수
    :param number: 검색할 게시글 번호
    :return: 검색된 게시글 정보
    """
    # post_info list안의 post 정보를 하나씩 가져와 post변수에 저장하고 반복문 안에서 사용
    for post in post_info:
        # post 정보안에 'number'라는 key의 value 값이 전달받은 number와 같다면,
        if post['number'] == number:
            # 해당 post 정보를 return
            return post


# 수정(번호로 정보 수정)
def update(number, title, content, file):
    """
    전달받은 number를 통해 select함수를 실행해서 해당 정보를 가져와
    매개변수의 내용으로 수정하는 함수
    :param number: 게시글 번호
    :param title: 수정할 게시글 제목
    :param content: 수정할 게시글 내용
    :param file: 수정할 첨부파일
    """
    # select함수를 통해 검색한 게시글 정보를 post에 저장
    post = select(number)
    post['title'] = title
    post['content'] = content
    post['file'] = file



# 삭제(번호로 삭제)
def delete(number):
    """
    전달받은 숫자로 게시글을 찾고 해당 정보를 post_info에서 삭제하는 메소드
    :param number: 삭제할 게시글 번호
    """
    # 1. select(number) - number를 통해 해당 게시글 정보 검색
    # 2. post_info.index() - 1번의 resturn 값으로 post_info안의 index 찾기
    # 3. del post_info[] - 2번의 index로 del함수 실행
    del post_info[post_info.index(select(number))]



insert(title='테스트 제목6', content='테스트 내용6', file='/usr/post/file/img006')
print(select_all())
print(select(2))
read(2)
print(select(2))
delete(2)
update(2, title='수정된 ')
print(select_all())