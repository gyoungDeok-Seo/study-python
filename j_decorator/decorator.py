# import datetime
#
# def log_time(original_function): 2
#     print('log_time 들어옴')2
#
#     def logging(*args):3
#         print('logging 들어옴')3
#         print(args)3
#         print(datetime.datetime.now())3
#         print('logging 함수 종료')3
#         return original_function(*args)3
#
#
#     print('log_time 함수 종료')2
#     return logging2
#
#
# @log_time 2
# def add(*args):4
#     total = 04
#     for i in args:4
#         total += i4
#
#     return total4
#
# result = add(1, 2, 3) 1
# print(result)

# 평균을 구해주는 데코레이터를 제작한다.
# 여러 개의 정수를 전달받으면, 총 합을 직접 구해준 뒤 평균을 출력한다.
# 총 합(total)과 개수(count)를 전달받으면, 총 합/개수로 평균을 출력한다.
# 총 합을 구하는 함수를 제작한 뒤 데코레이터를 통해 평균도 같이 확인할 수 있어야 한다.
# def average(original_function):
#     def operate(*args, **kwargs):
#         count = len(args)
#         result = 0
#
#         if count != 0:
#             for arg in args:
#                 result += arg
#             result /= count
#
#         else:
#             result = kwargs['total'] / kwargs['count']
#
#         result = round(result, 2)
#         print(f"평균: {result}")
#
#         return original_function(*args, **kwargs)
#
#     return operate
#
#
# @average
# def set_datas(*args, **kwargs):
#     result = 0
#     if len(args) != 0:
#         for arg in args:
#             result += arg
#     else:
#         result = kwargs.get('total')
#
#     print(f'총 합: {result}')
#
# set_datas(total=900, count=4)
# set_datas(90, 60, 70)
#
# # 강사님 코드
# def average(original_function):
#     def operate(*args, **kwargs):
#         count = len(args)
#         if count != 0:
#             total = 0
#             for i in args:
#                 total += i
#
#         else:
#             total = kwargs.get('total')
#             count = kwargs.get('count')
#
#         print(f"평균: {total / count}")
#
#         return original_function(*args, **kwargs)
#
#     return operate
#
#
# @average
# def set_datas(*args, **kwargs):
#     total = 0
#     for i in args:
#         total += i
#     print(f"총 합: {total if total != 0 else kwargs.get('total')}")
#
#
# set_datas(1, 2, 3, 4, 5)
# set_datas(total=100, count=5)
