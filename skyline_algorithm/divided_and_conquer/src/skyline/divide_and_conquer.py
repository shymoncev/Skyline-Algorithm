from src.utils.dnc_utils import divide, conquer


def dnc(datas):
    datas = divide(datas)  # 데이터 분할
    return conquer(datas)  # 정복


def m_partitioning_dnc(datas):
    datas = divide(datas)  # 데이터 1차 분할

    for i in range(len(datas)):
        datas[i] = divide(datas[i])  # 각 분할을 한 번 더 분할

    local_skyline = []
    for parts in datas:
        local_skyline.append(parts)

    datas = []
    skyline = []
    for part in local_skyline:
        for p in [part[1], part[2], part[3]]:
            datas += p
        skyline += dnc(datas)
    return dnc(skyline)
