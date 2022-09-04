import os

BASE_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.abspath(os.path.join(BASE_PATH, '03.in'))


def p1(bin_list):
    gamma_rate = [0] * len(bin_list[0])
    epsilon_rate = [0] * len(bin_list[0])
    for line in bin_list:
        num = [int(x) for x in list(line)]
        for i in range(len(num)):
            gamma_rate[i] += num[i]

    for i in range(len(gamma_rate)):
        gamma_rate[i] = round(gamma_rate[i] / len(bin_list))
        epsilon_rate[i] = 0 if gamma_rate[i] == 1 else 1
    gamma = ''.join(str(x) for x in gamma_rate)
    epsilon = ''.join(str(x) for x in epsilon_rate)
    return int(gamma, 2) * int(epsilon, 2)


def _filter_list(lst, indx=0, stop_indx=11, flag=1):
    one_lst = []
    zero_lst = []

    for line in lst:
        if int(line[indx]) == 1:
            one_lst.append(line)
        else:
            zero_lst.append(line)

    if indx == stop_indx or (len(one_lst) == 1 and len(zero_lst) == 1):
        if len(one_lst) >= len(zero_lst):
            return one_lst[0] if flag == 1 else zero_lst[0]
        else:
            return zero_lst[0] if flag == 1 else one_lst[0]

    if len(one_lst) >= len(zero_lst):
        return _filter_list(one_lst, indx+1, stop_indx, flag) if flag == 1 else _filter_list(zero_lst, indx+1, stop_indx, flag)  # noqa: E501
    else:
        return _filter_list(zero_lst, indx+1, stop_indx, flag) if flag == 1 else _filter_list(one_lst, indx+1, stop_indx, flag)  # noqa: E501


def p2(bin_list):
    oxy = _filter_list(bin_list)
    co = _filter_list(bin_list, flag=0)

    return int(oxy, 2) * int(co, 2)


if __name__ == '__main__':
    X = [x.strip() for x in open(FILE_PATH, 'r')]
    print(p1(X))
    print(p2(X))
