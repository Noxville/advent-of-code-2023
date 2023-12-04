import math

with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]


def to_ints(s):
    return list(map(int, s.strip().split(" ")))


def parse(card):
    sp = card.replace("Card ", "").replace("  ", " ").strip().split(":")
    wins, nums = to_ints(sp[1].split("|")[0]), to_ints(sp[1].split("|")[1])
    return len(set(nums) & set(wins))


if __name__ == "__main__":
    print(sum([math.floor((2 ** (-1 + parse(c)))) for c in ls]))
