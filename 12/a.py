from itertools import product


def s_to_ints(s):
    return list(map(int, s.split(',')))


with open('big') as fin:
    ls = [e.strip().split() for e in fin.readlines()]


def count_valid(s, cts):
    valid = 0
    for p in product('#.', repeat=s.count('?')):
        idx, tmp = 0, ''
        for c in s:
            if c == '?':
                tmp += p[idx]
                idx += 1
            else:
                tmp += c
        # print(tmp)
        if cts == [len(_) for _ in [sp for sp in tmp.split(".") if sp]]:
            valid += 1
    return valid


print(sum([count_valid(line[0], s_to_ints(line[1])) for line in ls]))
