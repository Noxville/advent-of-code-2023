with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]

BIG = 10 * 10
grid, min_x, max_x, min_y, max_y, expand_x, expand_y = set(), BIG, -BIG, BIG, -BIG, set(), set()
for y, line in enumerate(ls):
    empty = True
    for x, c in enumerate(line):
        if c == '#':
            empty = False
            grid.add((x, y))
            min_x, max_x, min_y, max_y = min(min_x, x), max(max_x, x), min(min_y, y), max(max_y, y)
    if empty:
        expand_y.add(y)
for x in range(min_x, 1 + max_x):
    empty = True
    for y in range(min_y, 1 + max_y):
        if (x, y) in grid:
            empty = False
    if empty:
        expand_x.add(x)


def calc_total_dist(multiplier):
    dist = 0
    for a in grid:
        for b in grid:
            if a < b:
                dist += abs(a[0] - b[0]) + abs(a[1] - b[1])
                dist += (multiplier - 1) * len(
                    [_x for _x in range(1 + min(a[0], b[0]), max(a[0], b[0])) if _x in expand_x])
                dist += (multiplier - 1) * len(
                    [_y for _y in range(1 + min(a[1], b[1]), max(a[1], b[1])) if _y in expand_y])
    return dist


print(calc_total_dist(2))
print(calc_total_dist(1000000))
