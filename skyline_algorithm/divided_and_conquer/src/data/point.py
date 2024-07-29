from typing import Union
import random


class Points:
    def __init__(
            self,
            datas: Union[list[list[Union[int, float]]]] = None,
            size: tuple = (2, 1000),
            range_: tuple[int, int] = (10, 100),
            random_seed: int = None
            ) -> None:
        if not datas:
            if random_seed:
                random.seed(42)
            self.data = [random.sample(range(range_[0], range_[1]), size[0])
                         for _ in range(size[1])]
        else:
            self.data = datas


if __name__ == '__main__':
    point = Points()
    print(point.data)
    point = Points(datas=[[1, 2], [3, 4]])
    print(point.data)
