# 상속 예제
# 게시글 - 댓글
# 게시글 번호와 댓글 번호는 자동 증가
# 게시글 class에 게시들 정보 출력 메소드를 만들고
# 댓글 class에서 정보 출력 메소드를 상속받고 댓글 정보 추가하여 출력


class Post:
    post_number = 0

    # 게시글: 게시글 번호, 작성자, 제목, 내용
    def __init__(self, writer: str, title: str, content: str):
        Post.post_number += 1
        self.number = Post.post_number
        self.writer = writer
        self.title = title
        self.content = content

    def print_info(self):
        print(self.number, self.writer, self.title, self.content)


class Reply(Post):
    reply_number = 0

    # 댓글: 댓글 번호, 게시글 번호, 작성자, 댓글 내용
    def __init__(self, writer: str, title: str, content: str, reply_content: str):
        super().__init__(writer, title, content)
        Reply.reply_number += 1
        self.reply_number = Reply.reply_number
        self.post_number = Post.post_number
        self.writer = writer
        self.reply_content = reply_content

    def print_info(self):
        super().print_info()
        print(self.reply_number, self.post_number, self.reply_content, self.writer)


reply = Reply('서경덕', '게시글 제목1', '게시글 내용1', '댓글 내용1')
reply.print_info()
print(reply.reply_content)
# 회원 정보 - 프로필
# 회원 번호와 프로필 번호는 자동 증가
# 매개변수는 kwargs 사용
# 회원 정보: 회원 번호, 이름, 나이, 주소
# 프로필: 프로필 번호, 회원 번호, 이미지 경로, 상태 메시지

# 회원 - 게시글
# 회원 정보: 회원 번호, 이름, 이미지 경로
# 게시글: 게시글 번호, 회원 번호, 제목, 내용
#
# 장소 - 예약
# 장소 대여: 회사 이름, 전화 번호,
# 예약:

# 요구 사항
#회원가입 페이지를 (클래스, 상속, 오버라이딩, while,if, for ... 등을 사용해서 한번 만들어보자)
#단 패스워드는 암호화 할 것 (아스키 코드) , 관리자 로그인 시에는 아이디 앞에 admin_을 붙여야 하며, 회원 삭제와 상품 목록 수정을 할 수 있다.

#메뉴 = 1. 회원가입 2. 유저 로그인 3. 유저 검색 4. 회원 탈퇴 5. 상품 구매 6. 상품 판매 7. 프로그램 종료
# while True:
