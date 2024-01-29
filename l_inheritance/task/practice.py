# 은행은 3개를 선언한다.
# 모든 은행 고객을 관리하는 DB를 2차원 list로 선언한다.
# 모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호 중복검사 서비스가 있다.
# 화면쪽 메뉴는 "계좌개설, 입금하기, 출금하기, 잔액조회, 계좌번호 찾기(새로운 계좌 설정, 핸드폰 번호로 서비스 이용가능), 나가기"로 구성되어 있다.
def check(*, key, value):
    # banks = [[{}, {}], [], []]
    for bank in Bank.banks:
        # bank = [{}, {}]
        for user in bank:
            if user[key] == value:
                return user

    return None


# 은행
#    예금주
#    계좌번호(중복 없음)
#    핸드폰번호(중복 없음)
#    비밀번호
#    통장잔고

class Bank:
    total_count = 3
    banks = [[] for i in range(total_count)]

    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        self.object = self
        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money

    @classmethod
    def open_account(cls, bank_choice, **kwargs):
        user = [ShinHan, KookMin, KaKao][bank_choice -1](**kwargs)
        cls.banks[bank_choice - 1].append(user.__dict__)
        return user


    @staticmethod
    def check_account_number(account_number):
        return check(key='account_number', value=account_number)

    @staticmethod
    def check_phone(phone):
        return check(key='phone', value=phone)

    def deposit(self, money):
        self.money += money

    def withdraw(self, money):
        self.money -= money

    def balance(self):
        return self.money

    def __str__(self):
        return f"{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}"

# 신한
#    입금 시 수수료 50%
class ShinHan(Bank):
    pass

# 국민
#    출금 시 수수료 50%
class KookMin(Bank):
    pass

# 카카오
#    잔액조회 재산 반토막
class KaKao(Bank):
    pass


if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    # while True:
    #     # 은행 메뉴
    #     bank_choice = int(input(bank_menu))
    #
    #     while True:
    #         # 서비스 메뉴
    #         pass
    # user[key]
    key = 'key'
    data = {'key': 'value'}
    print(data.get(key))
    print(data[key])
