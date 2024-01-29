# def set_key(key):
#     formatting = ''
#
#     # 클로저
#     def set_value(value):
#         nonlocal formatting
#         formatting = f'{key}: {value}'
#         return formatting
#
#     return set_value
#
# set_name = set_key('이름')
# formatting_name = set_name("서경덕")
# print(formatting_name)

# '나이': 00살
# set_age = set_key('나이')
# formatting_age = set_age(20)
# print(formatting_age)

# def set_key(key):
#     formatting = ''
#
#     # 클로저
#     def set_value(value):
#         nonlocal formatting
#         formatting = f'{key}: {value}'
#         return formatting
#
#     return set_value
#
# set_name = set_key('이름')
# formatting_name = set_name("한동석")
# print(formatting_name)
#
# # '나이: 00살'
# set_name = set_key('나이')
# formatting_age = set_name("20살")
# print(formatting_age)
#
# print(f'{formatting_name}\n{formatting_age}')

# 이름(name) 또는 주제(topic) 및 요약(point), 둘 중 하나를 전달할 수 있다.
# 제작하는 함수는 각각 아래와 같은 형식의 문자열로 변환한다.
# 함수1. "name, 전달받은 이름"
# 함수2. "전달받은 주제, 전달받은 요약"
# 구분점은 기본 값이 ', '이고 원하는 구분점을 전달받아서 변경할 수 있다.
# 함수1과 함수2를 합쳐서 하나의 함수로 만든다.
# 구분점은 각 함수에서 전달받는다.


# def set_topic(**kwargs):
#     result = 0
#
#     if 'name' in kwargs:
#         def set_name(dividing=', '):
#             formatting = f'name{dividing}{kwargs["name"]}'
#             return formatting
#
#         result = set_name
#     else:
#         def set_point(dividing=', '):
#             formatting = f'{kwargs["topic"]}{dividing}{kwargs["point"]}'
#             return formatting
#
#         result = set_point
#
#     return result
#
#
# print(set_topic(name='서경덕')('/'))
# print(set_topic(topic='마블', point='요즘 마블영화 챙기는 사람 없다.')('&'))


# 상품 정보(상품명, 가격)를 여러 개 전달받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.
def set_product(*args):
    number = 0

    for arg in args:
        number += 1
        arg['number'] = number

    def insert(**kwargs):
        nonlocal number,args
        number += 1
        args += {'name': kwargs['name'], 'price': kwargs['price'], 'number': number},

    def update(**kwargs):
        for product in args:
            if product['number'] == kwargs['number']:
                product['name'] = kwargs['name']
                product['price'] = kwargs['price']

    def select_all():
        return args

    return {'insert': insert, 'update': update, 'select_all': select_all}


products = [
    {'name': '모니터', 'price': 100000},
    {'name': '키보드', 'price': 50000}
]

new_product = {'name': '마우스', 'price': 10000}

product_service = set_product(*products)

print(product_service['select_all']())
product_service['insert'](**new_product)
print(product_service['select_all']())
product_service['update'](number=2, name='장패드', price=20000)
print(product_service['select_all']())