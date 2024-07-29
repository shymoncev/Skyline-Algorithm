import random
import matplotlib.pyplot as plt


def _dominates(point1: list, point2: list) -> bool:
    '''
    Check whether point1 dominate point2.

    Parametars
    ----------
    p1 : list
    p2 : list

    Returns
    -------
    bool
        If p1 dominates p2, return True, if not return False.
    '''
    if not len(point2):
        return True
    return (
        all(p1 <= p2 for p1, p2 in zip(point1, point2))  # p1의 x, y좌표가 p2보다 작거나 같은 경우...
        and any(p1 < p2 for p1, p2 in zip(point1, point2))  # p1이 x, y 중 하나라도 작으면 지배하는 것으로 판단
        )


def skyline(datas: list[list]) -> list[list]:
    '''
    Calculate the skyline points of the input datas

    Parameters
    ----------
    datas: list[list]

    Returns
    -------
    list[list]
    '''
    if (len(datas) == 1) or (len(datas) == 0):  # 비교 대상이 없으면 return
        return datas

    skyline_ = []
    candidates = datas[:]  # skyline 후보 list
    compared_points = datas[:]  # 비교 대상

    for p1 in candidates:
        if p1 in compared_points:
            compared_points.remove(p1)  # 비교 대상에는 자기 자신 제외
        for p2 in compared_points:
            if _dominates(p1, p2):  # p1이 p2를 지배하는 경우
                datas.remove(p2)  # 전체 데이터에서 p2를 삭제
                if p1 not in skyline_:
                    skyline_.append(p1)  # p1이 skyline에 없다면 추가
                if p2 in skyline_:
                    skyline_.remove(p2)  # p2가 skyline에 있다면 삭제
            else:
                if p2 not in skyline_:
                    skyline_.append(p2)  # 비교불가인 경우 p2를 skyline에 추가
        compared_points = datas[:]  # 비교 대상 초기화
    return skyline_


if __name__ == '__main__':
    try:
        if _dominates([1, 2], [3, 2]) is True:
            print('Function Well')
        else:
            print('Function has an error!')
    except Exception as e:
        print(e)

    datas = [random.sample(range(10, 1000), 2) for _ in range(100)]
    plt.scatter(
        x=[data[0] for data in datas],
        y=[data[1] for data in datas],
        color='black'
        )
    skyline_ = skyline(datas)
    plt.scatter(
        x=[data[0] for data in skyline_],
        y=[data[1] for data in skyline_],
        color='red'
        )
    plt.show()
    print(skyline_)
