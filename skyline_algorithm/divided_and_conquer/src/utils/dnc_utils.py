from typing import Union
import random
import numpy as np
import matplotlib.pyplot as plt
from src.utils.utils import skyline


def divide(
        datas: Union[list[list[Union[int, float]]]]
        ) -> Union[list[list[Union[int, float]]]]:
    X_median = np.median([data[0] for data in datas])
    y_median = np.median([data[1] for data in datas])

    # partitioning
    part0 = [[x, y]
             for x, y in datas
             if (x > X_median) and (y > y_median)]
    part1 = [[x, y]
             for x, y in datas
             if (x <= X_median) and (y > y_median)]
    part2 = [[x, y]
             for x, y in datas
             if (x <= X_median) and (y <= y_median)]
    part3 = [[x, y]
             for x, y in datas
             if (x > X_median) and (y <= y_median)]
    return [part0, part1, part2, part3]


def conquer(
        divided_datas: Union[list[list[Union[int, float]]]]
        ) -> list[list]:
    local_skylines = []  # 각 partition 별 local skyline 계산
    for part in divided_datas:
        local_skylines.append(skyline(part))
    datas = []
    for local in [local_skylines[1], local_skylines[2], local_skylines[3]]:
        datas += local  # 2, 3, 4사분면 데이터만 고려
    return skyline(datas)


if __name__ == '__main__':
    datas = [random.sample(range(10, 100), 2) for _ in range(1000)]
    plt.scatter(
        x=[data[0] for data in datas],
        y=[data[1] for data in datas],
        color='black'
        )
    data = divide(datas)
    print(
        data,
        skyline_ := conquer(data),
        sep='\n'
        )
    plt.scatter(
        x=[data[0] for data in skyline_],
        y=[data[1] for data in skyline_],
        color='red'
        )
    plt.show()
