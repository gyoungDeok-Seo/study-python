from typing import List, Dict, Set, Tuple, Union, Final

# 변경하지 말자는 약속
data: Final[int] = 10
print(data)

class A:
    pass


class B:
    @staticmethod
    def test(data: Union[int, str], number: int | float, data1: A, data2: List[int], data_dict: Dict[str, int]) -> int:
        return 10