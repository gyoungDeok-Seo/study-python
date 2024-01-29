from typing import List, Dict, Set, Tuple, Union, Final


# [종합 실습]

#

#
# 은행은 3개를 선언한다.
# 모든 은행 고객을 관리하는 DB를 2차원 list로 선언한다.
# 모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호 중복검사 서비스가 있다.
# 화면쪽 메뉴는 "계좌개설, 입금하기, 출금하기, 잔액조회, 계좌번호 찾기(새로운 계좌 설정, 핸드폰 번호로 서비스 이용가능), 나가기"로 구성되어 있다.
def check(number):
    result = {}
    for i in range(Bank.total_count):
        if len(Bank.banks[i]) == 0:
            return result

    for bank in Bank.banks:
        for i in range(len(bank)):
            if number == bank[i].account and number == bank[i].phone:
                return bank[i]
            else:
                return result




class Bank:
    total_count = 3
    banks = [[] for i in range(total_count)]

    def __init__(self, **kwargs):
        self.owner = kwargs['owner']
        self.account = kwargs['account']
        self.phone = kwargs['phone']
        self.password = kwargs['password']
        self.balance = kwargs['money']

        if kwargs['bank_name'] == '신한 은행':
            Bank.banks[0].append(self)

        elif kwargs['bank_name'] == '국민 은행':
            Bank.banks[1].append(self)

        else:
            Bank.banks[2].append(self)


    @classmethod
    def open_account(cls, **kwargs):
        if kwargs['bank_name'] == 1:
            kwargs['bank_name'] = '신한 은행'

        elif kwargs['bank_name'] == 2:
            kwargs['bank_name'] = '국민 은행'

        else:
            kwargs['bank_name'] = '카카오 뱅크'

        return cls(**kwargs)

    @staticmethod
    def check_account_number(account):
        if len(check(account)) != 0:
            return check(account)
        return check(account)

    @staticmethod
    def check_phone(phone):
        return check(phone)


    def deposit(self):
        pass

    def withdraw(self):
        pass

    def balance(self):
        pass

    def __str__(self):
        return f'예금주: {self.owner}, 계좌번호: {self.account}, 전화번호: {self.phone}, 비밀번호: {self.password}, 통장잔고: {self.balance}'


class ShinHan(Bank):
    deposit_fee = 50


class KookMin(Bank):
    withdraw_fee = 50


class KaKao(Bank):
    balance_fee = 50


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

    while True:
        # 은행 메뉴
        choice = int(input(bank_menu))

        if choice in [1, 2, 3]:
            while True:
                # 서비스 메뉴
                service = int(input(menu))

                if service == 1:
                    owner = input(owner_message)
                    account = input(account_number_message)
                    phone = input(phone_message)
                    password = input(password_message)
                    money = int(input(money_message))
                    new_account = {
                        'bank_name': choice,
                        'owner': owner,
                        'account': account,
                        'phone': phone,
                        'password': password,
                        'money': money
                    }
                    if check(**new_account):
                        print(error_message)
                        continue

                    new_owner = ShinHan.open_account(**new_account)
                    print(new_owner)

                elif service == 2:
                    account = input(account_number_message)
                    password = input(password_message)

                elif service == 3:
                    pass

                elif service == 4:
                    pass

                else:
                    break

        elif choice == 4:
            break

        else:
            print(error_message)
            continue
