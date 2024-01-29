# 중복 검사(강사님 주석)
# 핸드폰 번호와 계좌 번호를 검색할 수 있다.
# 정확히 어떤 것을 검사할 지는 사용자에세 전달받은 key로 확인할 수 있다.
def check(*, key: str, value: str) -> dict:
    """
    key와 value를 전달받고 이중for문으로 검색하여 예금주의 정보를 return
    :param key: 검사할 key 값
    :param value: 검사할 value 값
    :return: 예금주의 정보(dict)
    """
    # (강사님)저장소(DB)에서 각 은행 정보를 가져온 뒤
    # (나)Bank의 정적 변수 banks의 은행별 회원 정보들의 bank로 가져와 사용하는 for문
    for bank in Bank.banks:
        # (강사님)각 은행에서 회원의 정보를 가져온다.
        # (나)은행별 회원 정보들(list) 중 각각의 회원 정보(dict)를 가져와 user로 사용하는 for문
        for user in bank:
            # (강사님)전달받은 키워드(key)로 회원의 정보가 value와 같은 지 검사한다.
            # (나)user에 매개변수 key로 저장된 value 중 배개변수 value와 같은 것이 있다면,
            if user[key] == value:
                # (강사님)만약 해당 회원을 찾았다면, 회원의 전체 정보를 리턴한다.
                # (나)해당 user를 return
                return user
    # (강사님)해당 회원을 찾지 못했다면, None을 리턴한다.
    # (나)위 if문에 들어가지 않았다면 None return
    # (나)None은 주소값의 초기값이다.
    return None


class Bank:
    # 클래스 변수
    total_count = 3
    # comprehention을 사용하여 total_count만큼 2차행렬 list생성
    banks = [[] for i in range(total_count)]
    # Bank 클래스를 객체화 할 때 필드를 구성하는 생성자
    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        # self.이 붙은 것들은 객체화 되는 객체의 주소값을 통해 객체를 특정하고 해당 필드에 값을 저장하기 위해 사용
        # self.object는 객체를 클래스 변수 banks에 저장할 때 __dict__ magic_method를 사용해서
        # dict로 변환하여 저장하기 때문에 객체의 주소를 저장하기 위해 사용
        self.object = self
        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money

    @classmethod
    def open_account(cls, bank_choice, **kwargs):
        """
        전달받은 은행번호와 kwargs를 사용해서 해당 자식 클래스로 객체화하고 클래스 변수에 저장하도록 wrapping하는 메소드
        :param bank_choice: 은행 선택 번호
        :param kwargs: 예금주: owner, 계좌번호: account_number, 전화번호: phone, 비밀번호: password, 예치금: money
        :return: 은행 객체
        """
        # 자식 클래스들을 list에 담고 bank_choice로 index를 구분하고 매개변수kwargs로 bank객체 객체화
        bank = [ShinHan, KookMin, KaKao][bank_choice - 1](**kwargs)
        # 클래스 변수 banks의 index를 bank_choice로 구분하여 객체를 dict로 만들어 추가
        cls.banks[bank_choice - 1].append(bank.__dict__)
        # 재정의 된 __str__을 사용하기 위해 객체를 return
        return bank

    @staticmethod
    def check_account_number(account_number: str) -> dict:
        """
        account_number를 통해 중복검사를 실행하고 해당하는 dict를 return하는 메소드
        :param account_number: 계좌번호
        :return: 전달받은 계좌번호에 갖고있는 dict
        """
        # check함수를 통해 전달받은 dict, 또는 None을 return
        return check(key='account_number', value=account_number)

    @staticmethod
    def check_phone(phone: str) -> dict:
        """
        phone을 통해 중복검사를 실행하고 해당하는 dict를 return 하는 메소드
        :param phone: 전화번호
        :return: 전달받은 전화번호를 갖고있는 dict
        """
        # check함수를 통해 전달받은 dict, 또는 None을 return
        return check(key='phone', value=phone)

    def deposit(self, money: int):
        """
        전달받은 금액을 필드의 잔액에 더하고 저장하는 메소드
        :param money: 입금할 금액
        """
        # self를 통해 필드에 접근하여 기존 필드값과 매개변수를 더하고 저장
        self.money += money

    def withdraw(self, money: int):
        """
        전달받은 금액을 필드의 잔액에서 빼고 저장하는 메소드
        :param money: 출금할 금액
        """
        # self를 통해 필드에 접근하여 기존 필드값에서 매개변수를 빼고 저장
        self.money -= money

    def balance(self):
        """
        필드에 접근하여 잔액을 조회하는 메소드
        :return: 잔액
        """
        # self를 통해 필드에 접근하여 기존 필드값을 가져와 return
        return self.money

    def __str__(self):
        """
        객체를 출력할 때 출력되는 값을 재정의 하는 메소드
        :return: 예금주의 이름, 계좌번호, 전화번호, 비밀번호, 잔액
        """
        # self로 객체에 접근하여 각 필드명으로 불러와 서식문자로 return
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'


# Bank클래스를 상속 받은 ShinHan클래스
# 객체화는 상속 받아 사용할 수 있고 따로 추가할 내용이 없기 때문에 별도로 생성자를 재정의 하지 않음
# 해당 클래스는 입금 수수료가 별도로 있어 deposit메소드를 재정의하여 사용
class ShinHan(Bank):
    def deposit(self, money: int):
        """
        부모 클래스에서 선언된 deposit메소드를 입금 수수료가 적용되도록 재정의한 메소드
        :param money: 입금할 금액
        """
        # 입금 수수료가 50%로 입금할 금액을 반으로 나눈 몫을 money에 저장
        # 나눈 값이 실수가 될 경우를 방지하기 위해 몫 연산자를 사용
        money //= 2
        # 부모 클래스의 deposit메소드 실행
        super().deposit(money)


# Bank클래스를 상속 받은 KookMin클래스
# 객체화는 상속 받아 사용할 수 있고 따로 추가할 내용이 없기 때문에 별도로 생성자를 재정의 하지 않음
# 해당 클래스는 출금 수수료가 별도로 있어 withdraw메소드를 재정의하여 사용
class KookMin(Bank):
    def withdraw(self, money: int):
        """
        부모 클래스에서 선언된 withdraw메소드를 출금 수수료가 적용되도록 재정의한 메소드
        :param money: 출금할 금액
        """
        # 출금 수수료가 50%로 출금할 때 수수료도 함께 계산되도록 계산하고 money에 저장
        money *= 1.5
        # 부모 클래스의 withdraw메소드를 실행하되 money가 정수와 실수의 연산으로 실수가 되기 때문에 int로 형변환하여 사용
        super().withdraw(int(money))


# Bank클래스를 상속 받은 KaKao클래스
# 객체화는 상속 받아 사용할 수 있고 따로 추가할 내용이 없기 때문에 별도로 생성자를 재정의 하지 않음
# 해당 클래스는 잔액 조회 수수료가 별도로 있어 balance메소드를 재정의하여 사용
class KaKao(Bank):
    def balance(self):
        """
        부모 클래스에서 선언된 balance메소드를 잔액 조회 수수료가 적용되도록 재정의한 메소드
        :return: 조회 수수료가 적용된 잔액
        """
        # 조회 수수료가 50%로 조회할 때 수수료도 함꼐 계산하고 해당 필드값에 저장
        self.money //= 2
        # 부모 클래스의 balance메소드를 실행하여 잔액 return
        return super().balance()

# 메인 소스코드임을 명시하기 위해 사용
if __name__ == '__main__':
    # 은행 메뉴와 번호를 보여주는 메시지
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    # 서비스 메뉴와 번호를 보여주는 메시지
    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 계좌 번호 재설정\n" \
           "6. 은행 선택 메뉴로 돌아가기\n"

    # 예금주 입력 시 출력될 메시지
    owner_message = "예금주: "
    # 계좌번호 입력 시 출력될 메시지
    account_number_message = "계좌번호: "
    # 핸드폰 번호 입력 시 출력될 메시지
    phone_message = "핸드폰 번호: "
    # 비밀번호 입력 시 출력될 메시지
    password_message = "비밀번호(4자리): "
    # 예치금 입력 시 출력될 메시지
    money_message = "예치금: "
    # 입금액 입력 시 출력될 메시지
    deposit_message = "입금액: "
    # 출금액 입력 시 출력될 메시지
    withdraw_message = "출금액: "
    # 잘못 입력했거나 중복검사에 걸릴 경우 출력할 메시지
    error_message = "다시 시도해주세요"

    # 특정 상황에서 반복을 멈추기 위해 while문으로 조건식을 True로 설정
    while True:
        # 은행 메뉴
        # 입력 받은 은행 번호를 int로 형변환하여 bank_choice에 저장
        bank_choice = int(input(bank_menu))
        # bank_choice가 4라면
        if bank_choice == 4:
            # 반복 종료
            break
        # bank_choice가 1~3이라면(강사님이 주신 코드 중 1~4이외의 숫자를 입력해도 코드가 실행되어 추가)
        if bank_choice in [i + 1 for i in range(Bank.total_count)]:
            # 특정 상황에서 반복을 멈추기 위해 while문으로 조건식을 True로 설정
            while True:
                # 서비스 메뉴
                # 입력 받은 서비스 번호를 int로 형변환하여 menu_choice에 저장
                menu_choice = int(input(menu))
                # menu_choice가 5라면
                if menu_choice == 6:
                    # 밖앗 while문으로 나가기
                    break

                # 개설
                if menu_choice == 1:
                    # 입력 받은 예금주명을 owner에 저장
                    owner = input(owner_message)
                    # 계좌번호 중복검사를 반복하기 위해 사용
                    while True:
                        # 입력받은 계좌번호를 account_number에 저장
                        account_number = input(account_number_message)
                        # Bank클래스 check_account_number 메소드의 return 값이 None이라면, 계좌번호 중복검사 종료
                        # return 값이 None이 아니라면, 반복 진행
                        if Bank.check_account_number(account_number) is None:
                            break
                    # 전화번호 중복검사를 반복하기 위해 사용
                    while True:
                        # 입력받은 전화번호를 phone에 저장
                        phone = input(phone_message)
                        # Bank클래스 check_phone메소드의 return 값이 None이라면, 전화번호 중복검사 종료
                        # return 값이 None이 아니라면, 반복 진행
                        if Bank.check_phone(phone) is None:
                            break
                    # 비밀번호 자릿수를 맞추기 위해 반복 사용
                    while True:
                        # 입력받은 비밀번호를 password에 저장
                        password = input(password_message)
                        # password의 길이가 4라면, 반복 종료
                        # 4가 아니라면 비밀번호 다시 입력 받기
                        if len(password) == 4:
                            break
                    # 에치금을 입력받고 money에 저장
                    money = int(input(money_message))
                    # Bank클래스에 open_account메소드를 통해 wrapping하여 객체화
                    user = Bank.open_account(
                        bank_choice, owner=owner, account_number=account_number,
                        phone=phone, password=password, money=money
                    )
                    # Bank클래스에서 __str__메소드 통해 재정의한 string을 출력
                    # 예금주명, 계좌번호, 전화번호, 비밀번호, 잔액
                    print(user)

                # 입금
                # 개설한 은행에서만 입금 가능
                elif menu_choice == 2:
                    # 입력받은 계좌번호를 account_number에 저장
                    account_number = input(account_number_message)
                    # Bank클래스 check_account_number메소드로 찾은 예금주 정보를 user에 저장
                    user = Bank.check_account_number(account_number)
                    # user가 None이 아니라면,
                    if user is not None:
                        # user['password']의 value 값과 입력받은 비밀번호가 같다면,
                        if user['password'] == input(password_message):
                            # 삼항식을 사용하여 bank_choice의 값에 따라 선택한 은행type을 class_type에 저장
                            class_type = ShinHan if bank_choice == 1 else (
                                KookMin if bank_choice == 2 else KaKao
                            )
                            # class_type과 user를 이용하여 선택한 은행과 입금하려는 통장이 같은 은행이라면,
                            # class_type의 타입과 user의 타입을 isinstance함수를 사용하여 타입을 비교
                            if isinstance(user['object'], class_type):
                                # input함수로 받은 값(입금액)은 str타입 임으로 int로 형변환하고 deposit_money에 저장
                                deposit_money = int(input(deposit_message))
                                # 'object'라는 키 값으로 저장한 객체의 주소를 통해 deposit메소드 실행
                                user['object'].deposit(deposit_money)
                                # 다시 서비스 메뉴로 이동(반복 진행)
                                continue
                            # class_type과 user를 이용하여 선택한 은행과 입금하려는 통장 은행이 같은 은행이 아니라면,
                            # 에러 메시지 출력하고 반복 진행
                            print('개설한 은행에서만 입급 서비스를 사용하실 수 있습니다.')
                    # user가 None이라면,
                    # 에러 메시지 출력하고 반복 진행
                    print(error_message)

                # 출금
                elif menu_choice == 3:
                    # 입력받은 계좌번호를 account_number에 저장
                    account_number = input(account_number_message)
                    # Bank클래스의 check_account_number메소드를 사용하여 찾은 예금주 정보를 user에 저장
                    user = Bank.check_account_number(account_number)
                    # user가 None이 아니라면,
                    if user is not None:
                        # user['password']의 value 값과 입력받은 비밀번호가 같다면,
                        if user['password'] == input(password_message):
                            # input함수로 받은 값은 str타입이기 때문에 int로 형변환하여 withdraw_money에 저장
                            withdraw_money = int(input(withdraw_message))
                            # user의 타입이 KookMin이라면 withdraw_money에 1.5를, KookMin이 아니라면 1을 곱하고
                            # 곱한 것 보다 user['money']의 value 값이 더 작거나 같다면,
                            if withdraw_money * (1.5 if isinstance(user['object'], KookMin) else 1) <= user['money']:
                                # object라는 키값으로 저장한 객체의 주소로 접근하여 withdraw메소드를 실행
                                user['object'].withdraw(withdraw_money)
                                # 다시 서비스 메뉴로 이동(반복 진행)
                                continue
                            # 곱한 것 보다 user['money']의 value 값이 더 크다면,
                            else:
                                # 에러 메시지 출력하고 반복 진행
                                print(error_message)
                    # user가 None이라면,
                    else:
                        # 에러 메시지 출력하고 반복 진행
                        print(error_message)

                # 잔액 조회
                elif menu_choice == 4:
                    # 입력받은 계좌번호를 account_number에 저장
                    account_number = input(account_number_message)
                    # Bank클래스의 check_account_number메소드를 사용하여 찾은 예금주 정보를 user에 저장
                    user = Bank.check_account_number(account_number)
                    # user가 None이 아니라면,
                    if user is not None:
                        # user['password']의 value 값과 입력받은 비밀번호가 같다면,
                        if user['password'] == input(password_message):
                            # object라는 키값으로 저장한 객체의 주소로 접근하여 balance메소드를 실행하고 return된 잔액을 서식문자로 출력
                            print(f'현재 잔액: {user["object"].balance()}')
                            # 다시 서비스 메뉴로 이동(반복 진행)
                            continue
                    # user가 None이라면,
                    else:
                        # 에러 메시지 출력하고 반복 진행
                        print(error_message)

                # 계좌 번호 재설정
                # 핸드폰 번호, 비밀번호 입력 후
                # 정확하면, 해당 회원의 계좌번호 재설정(다시 입력받기)
                elif menu_choice == 5:
                    # 입력받은 전화번호를 phone에 저장
                    phone = input(phone_message)
                    # check함수를 사용하여 phone과 같은 value 값을 같고있는 예금주 정보를 찾고 user에 저장
                    user = Bank.check_phone(phone)
                    # user가 None이 아니라면,
                    if user is not None:
                        # user['password']의 value 값과 입력받은 비밀번호가 같다면,
                        if user['password'] == input(password_message):
                            # 새로운 계좌번호 중복 검사 반복
                            while True:
                                # 입력받은 계좌번호를 new_account_number에 저장
                                new_account_number = input(account_number_message)
                                # 새로운 계좌번호가 기존 계좌번호들과 중복되지 않는다면,
                                if Bank.check_account_number(new_account_number) is None:
                                    # 다시 서비스 메뉴로 이동(반복 진행)
                                    break
                                # 새로운 계좌번호가 기존 계좌번호들과 중복된다면, 출력 후 다음 반복
                                print('중복되는 계좌번호가 있습니다.')
                                continue
                            # user['object']의 value값 예금주 객체에 접근하여 필드값을 new_account_number로 변경
                            user['object'].account_number = new_account_number
                            # Bank 클래스에서 __str__메소드가 재정의 되어 변경된 예금주 정보 출력
                            print(user['object'])

                    # user가 None이라면,
                    else:
                        # 에러 메시지 출력하고 반복 진행
                        print(error_message)

                # menu_choice가 1 ~ 6이 아니라면
                else:
                    # 에러 메시지 출력하고 반복 진행
                    print(error_message)
        # bank_choice가 1 ~ 4가 아니라면
        else:
            # 에러 메시지 출력하고 반복 진행
            print(error_message)
