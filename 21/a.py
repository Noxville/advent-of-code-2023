BIG = 26501365


def neigh(_x, _y):
    return [
        (_x + 1, _y),
        (_x - 1, _y),
        (_x, _y + 1),
        (_x, _y - 1),
    ]


def part1(grid, start):
    flood = {start}  # only keep one iteration at a time
    for i in range(64):
        new_flood = set()
        for f in flood:
            for n in neigh(*f):
                if n in grid:
                    new_flood.add(n)
        flood = new_flood
    return len(flood)


def differences(ln):
    return [z[1] - z[0] for z in zip(ln, ln[1:])]


def part2(grid, start, size):
    parity = BIG % size
    flood = {start}
    terms = []
    for i in range(3 * size - parity):  # we need 3 terms to solve the equation
        if i % size == parity:
            # print(len(flood))
            terms.append(len(flood))

        new_flood = set()
        for f in flood:
            for n in neigh(*f):
                if (n[0] % size, n[1] % size) in grid:
                    new_flood.add(n)
        flood = new_flood

    d1 = differences(terms)
    d2 = differences(d1)
    a = d2[0] // 2

    minus_an2 = [_ - (a * ((n + 1) ** 2)) for n, _ in enumerate(terms)]
    b = differences(minus_an2)[0]
    c = terms[0] - a - b
    n = 1 + (BIG // size)
    # print(a, b, c)
    return a * n ** 2 + b * n + c


with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]
    g = set()
    for y, line in enumerate(ls):
        for x, char in enumerate(line):
            if char == 'S':
                sx, sy = x, y
                g.add((x, y))
            elif char != '#':
                g.add((x, y))
    print(part1(g, (sx, sy)))
    print(part2(g, (sx, sy), len(ls)))
