# 강사님 코드
# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.

# 입력 예시1
# [2000, 4000, 5000]
# coupon=50
# count=2

# 출력 예시1
# [1000, 2000]

# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100

# 출력 예시2
# [700, 2800, 3500]

# 매개변수를 packing(args)과 kwargs로 전달받고 할인율이 적용된 금액을 return하는 use_coupon함수를 선언
# 금액들은 한번에 전달 받고 iterator로 사용하기 위해 packing(args)으로 받는다.
# 쿠폰 개수와 할인율은 정확하게 전달받고 사용하기 위해 dict형태의 kwargs로 받는다.
def use_coupon(*pay, **kwargs):
    # 함수 안에서 여러줄 주석을 사용할 경우 함수 및 전달 받는 매개변수, return 값에 대한 설명을 작성할 수 있다.
    # 여러줄 주석으로 작성한 설명은 help(함수명)으로 사용할 수 있다
    '''

    :param pay: 주문 금액들
    :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
    :return: 할인율이 적용된 주문 금액들
    '''
    # 매개변수로 받은 kwargs에 'coupon'이라는 키값이 있다면,
    if 'coupon' in kwargs:
        # comprehension으로 반복문을 진행하여 할인율이 적용된 값들을 list에 담아서 return
        return [
            # kwargs안에 'coupon'이라는 key값으로 저장된 value값을 가져와서 할인 금액을 구한다.
            int((1 - kwargs.get('coupon') * 0.01) * pay[i])
            # 반복문을 실행
            for i in
            # 반복문의 iterator로 range함수를 사용
            # index오류가 발생하는 상황이 있어서 삼항연산자로 매개변수 처리
            # 쿠폰의 수 보다 금액들의 개수가 더 크거나 같다면 쿠폰의 개수를, 작다면 금액들의 개수를 매개변수로 사용
            range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))
        ]
    # 매개변수로 받은 kwargs에 'coupon'이라는 키값이 없다면, None을 return
    return None

# 함수에 대한 설명 확인
help(use_coupon)
# use_coupon함수를 사용하고 나온 return 값을 result에 저장
result = use_coupon(1000, 2000, 3000, coupon=50, count=100)
# 만약 result에 값이 있다면, result 출력
if result:
    print(result)
# reulst에 값이 없다면, '쿠폰이 없습니다.' 출력
else:
    print('쿠폰이 없습니다.')
