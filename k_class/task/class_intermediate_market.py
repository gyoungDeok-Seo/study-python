# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수
class Product:
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def product_info(self):
        print(f'상품명: {self.product_name}, 가격: {self.product_price}원')


# 손님
# 이름, 나이, 할인율, 잔액
class Customer:
    def __init__(self, name, age, discount=0, money=0):
        self.name = name
        self.age = age
        self.discount = discount
        self.money = money

# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.
class Mart:
    def __init__(self, product, stock):
        self.product = product
        self.stock = stock

    def sell_for_user(self, customer):
        discount_price = int(self.product.product_price * (1 - customer.discount * 0.01))
        customer.money -= discount_price
        self.stock -= 1
        result = self.product.product_name, self.product.product_price, discount_price, customer.money
        return result


ryo = Customer('Ryo', 20, 40, 60000)
apple = Product('사과', 3000)
mart = Mart(apple, 30)

apple.product_info()
print(mart.stock)
print(mart.sell_for_user(ryo))
print(mart.stock)
print(ryo.money)
