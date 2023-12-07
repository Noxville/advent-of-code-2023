from functools import reduce


def nums(s):
    out = []
    for _ in s.split(" "):
        try:
            out.append(int(_))
        except ValueError:
            pass
    return out


def race(time, min_distance):
    return len([_t for _t in range(1 + time) if _t * (time - _t) > min_distance])


if __name__ == "__main__":
    with open('big') as fin:
        ls = [nums(e.strip()) for e in fin.readlines()]
    print(reduce((lambda x, y: x * y), [race(t, d) for t, d in zip(ls[0], ls[1])]))
