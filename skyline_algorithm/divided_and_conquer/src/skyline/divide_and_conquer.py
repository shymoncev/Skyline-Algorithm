from src.utils.dnc_utils import divide, conquer


def dnc(datas):
    return conquer(divide(datas))  # 분할 정복


def m_partitioning_dnc(datas):
    datas = divide(datas)  # 데이터 1차 분할
    for i in range(len(datas)):
        datas[i] = divide(datas[i])  # 각 분할을 한 번 더 분할

    local_skyline = []
    for part in datas:
        partitions = []
        for p in [part[1], part[2], part[3]]:
            partitions += p
        local_skyline += dnc(partitions)  # local skyline 계산

    return dnc(local_skyline)
