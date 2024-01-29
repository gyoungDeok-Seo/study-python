# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.

def discount(*args, **kwargs):
    '''
    회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하고
    할인율이 적용된 주문 금액이 정수로 리턴
    :param args: 주문 금액들(list)
    :param kwargs: 회원의 쿠폰 할인율(coupon)과 개수(count)
    :return: 할인율이 적용된 주문 금액들(list)
    '''
    # 풀어쓴 코드
    # 주문 금액의 length와 쿠폰 개수를 비교하여 더 작은 쪽의 숫자만큼 반복
    # if len(args) >= kwargs['count']:
    #     result = [0] * kwargs['count']
    # else:
    #     result = [0] * len(args)
    # 할인율이 적용된 주문 금액들을 리턴하기 위해 빈 list 선언
    result = []
    # 전달 받은 매개변수에서 kwargs['count']를 사용하여 쿠폰의 개수 만큼만 반복
    for i in range(kwargs['count']):
        # 주문 금액의 개수 보다 쿠폰 개수가 더 많을 경우 args[i]가 인덱스 초과로 오류가 발생하는 것을 막기 위해 제한
        if len(args) >= i + 1:
            # 실수와 정수의 연산으로 float타입으로 변한 값을 정수로 형변환해서 pay에 저장
            pay = int(args[i] - (args[i] * (0.01 * kwargs['coupon'])))
            # 위에서 선언한 result에 index로 수정
            # result[i] = pay
            # 위에서 선언한 result에 pay를 append로 추가
            result.append(pay)
        # 주문 금액의 개수 보다 쿠폰 개수가 더 많을 경우 불필요한 반복을 진행하지 않기 위해 break사용
        else:
            break
    # 할인율이 적용된 주문 금액 list를 리턴
    return result

    # comprehension
    # return [int(args[i] - (args[i] * (0.01 * kwargs['coupon']))) for i in range(kwargs['count']) if len(args) >= i + 1]


# 입력 예시1
# [2000, 4000, 5000]
# coupon=50
# count=2
args1 = [2000, 4000, 5000]
kwargs1 = {
    'coupon': 50,
    'count': 2
}

# 출력 예시1
# [1000, 2000]
print(discount(2000, 4000, 5000, coupon=50, count=2))
print(discount(*args1, **kwargs1))

# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100
args2 = [1000, 4000, 5000]
kwargs2 = {
    'coupon': 30,
    'count': 100
}

# 출력 예시2
# [700, 2800, 3500]
print(discount(1000, 4000, 5000, coupon=30, count=100))
print(discount(*args2, **kwargs2))

# help(discount)


# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.
# def use_coupon(*args, **kwargs):
#     '''
#
#     :param args: 주문 금액들
#     :param kwargs: {'coupon': 할인율, 'count': 쿠폰 개수}
#     :return: 할인율이 적용된 주문 금액들(list)
#     '''
#     if 'coupon' in kwargs:
#         return [
#             args[i] * (1 - kwargs['coupon'] * 0.01)
#             for i in
#             range(kwargs['count'] if kwargs.get('count') <= len(args) else len(args))
#         ]
#
#     return None

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