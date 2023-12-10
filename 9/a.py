with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]


def solve(row):
    delta = [y - x for x, y in zip(row, row[1:])]
    return (solve(delta) + row[-1]) if len(row) else 0


for direct in [1, -1]:
    nums = [list(map(int, line.split(' '))) for line in ls]
    print(sum([solve(n[::direct]) for n in nums]))
