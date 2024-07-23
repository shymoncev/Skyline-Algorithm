def check(datas):
    check_list = []
    checks = datas['partition'].value_counts()
    for index in checks.index:
        if checks[index] > 1:
            check_list.append(index)
    return check_list
