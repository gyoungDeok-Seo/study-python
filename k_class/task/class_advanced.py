# 회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다(class method).
class User:
    # private: 자신의 클래스에서만 접근 가능
    # 1. 외부에서 접근하지 말자!
    # 2. 외부에서 접근할 때 꼭 메소드로 접근하자!
    # 3. 메소드에 사용될 경우 절대 외부에서 사용하지 말자!
    __number = 0

    def __init__(self, **kwargs):
        User.__number += 1

        self.number = User.__number
        self.id = kwargs['id']
        self.password = kwargs['password']
        self.name = kwargs['name']

    @staticmethod
    def get_number():
        return User.__number


    @classmethod
    def admin_join(cls, **kwargs):
        kwargs['id'] = 'admin_' + kwargs['id']
        return cls(**kwargs)

    def print_user(self):
        print(self.number, self.id, self.password, self.name)


seo = User(id='qwer1234', password='1234', name='서경덕')
admin = User.admin_join(id='asdf5678', password='1234!@', name='관리자')
seo.print_user()
admin.print_user()