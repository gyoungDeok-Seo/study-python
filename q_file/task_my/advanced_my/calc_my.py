# 사용하는
from q_file.task_my.advanced_my.log_my import log_time


class Calculator:
    def __init__(self, number):
        self.oper = None
        self.number = number

    def calc(self, other, oper, error_cord=""):
        oper_number = {'+': 0, '-': 1, '*': 2, '/': 3}
        self.oper = oper
        return [self.__add__, self.__sub__, self.__mul__, self.__floordiv__][oper_number[oper]](other, error_cord=error_cord)

    @log_time
    def __add__(self, other, **kwargs):
        pass

    @log_time
    def __sub__(self, other, **kwargs):
        pass

    @log_time
    def __mul__(self, other, **kwargs):
        pass

    @log_time
    def __floordiv__(self, other, **kwargs):
        # 몫과 나머지 모두 구현
        pass

