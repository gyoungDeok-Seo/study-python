# 인간(부모)
# 이름, 나이
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# 걷기(walk)
# '두 발로 걷습니다.' 출력
    def walk(self):
        print("두 발로 걷습니다.")

# 원숭이(자식)
# 이름, 나이, 동물원 이름
class Monkey(Person):
    def __init__(self, name, age, zoo):
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.zoo = zoo

# 걷기(walk)
# '두 발로 걷습니다.', '네 발로 걷습니다.' 출력

    def walk(self):
        super().walk()
        print('네 발로 걷습니다.')

person = Person('서경덕', 29)
person.walk()
print(person.name, person.age)

monkey = Monkey('몽키', 10, '에버렌드')
monkey.walk()
print(monkey.name, monkey.age, monkey.zoo)
print(monkey.name, monkey.age, monkey.zoo)