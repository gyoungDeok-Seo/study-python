# unpacking: 값을 풀어서 적는 것
# def get_total(number1, number2, number3):
#     return number1 + number2 + number3


# packing: 값을 묶어서 적는 것
# def get_total(*numbers):
#     # 외부에서 전달받은 값들이 numbers(튜플)에 저장된다.
#     print(type(numbers))
#     total = 0
#     for number in numbers:
#         total += number
#
#     return total


# 여러 개의 값을 콤마로 구분하여 전달한다.
# total = get_total(1, 2, 3, 4, 5)
# print(total)


# 여러 개의 값을 하나로 묶어서 전달하게 되면, packing으로 인해 첫번째 방에 통채로 들어가게 된다.
# 즉, 결과는 다음과 같다. ([1, 2, 3, 4, 5], )
# 따라서 내부의 요소를 각각 전달하고 싶다면, 앞에 *을 작성해야 한다.
# numbers = [1, 2, 3, 4, 5]
# total = get_total(*numbers)
# print(total)

# 국어, 영어, 수학 점수를 전달받은 뒤 총 점을 출력하는 함수
# packing으로 제작하기
def sum(name, *scores): # 반드시 받아야 하는 매개변수는 packing 앞에 작성한다.
    print(name + '님')
    result = 0
    for score in scores:
        result += score

    return result

# 문자열에서 'A'가 몇 개 있는 지 검사하는 함수
# packing으로 제작하기
def find(*targets):
    return [target.count("A") for target in targets]

print(sum('서경덕',90, 90, 90))
numbers = [90, 90, 90]
print(sum('서경덕', *numbers))

print(find('AAA', 'AAB', 'ABC'))
targets = ['AAA', 'AAB', 'ABC']
# targets = {"문자열": "apple", "문자": 'e'}
print(find(*targets))