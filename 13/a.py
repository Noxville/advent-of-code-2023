from itertools import groupby


def solve(cs, allowed_wrong):
    mx, my, spots = len(cs[0]), len(cs), set()

    for y, line in enumerate(cs):
        for x, c in enumerate(line):
            if c == '#':
                spots.add((x, y))

    score = 0
    for c in range(mx - 1):
        wrong = 0 #False
        for dx in range(mx):
            l, r = c - dx, 1 + c + dx
            if r > l and l >= 0 and mx > r:
                for y in range(my):
                    if ((l, y) in spots) != ((r, y) in spots):
                        wrong += 1
        if wrong == allowed_wrong:
            score += 1 + c

    for r in range(my - 1):
        wrong = 0
        for dy in range(my):
            u, d = r - dy, 1 + r + dy
            if d > u and u >= 0 and my > d:
                for x in range(mx):
                    if ((x, u) in spots) != ((x, d) in spots):
                        wrong += 1
        if wrong == allowed_wrong:
            score += (1 + r) * 100
    return score


with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]

    cases = [list(s) for e, s in groupby(ls, key=bool) if e]
    print(sum([solve(case, 0) for case in cases]))
    print(sum([solve(case, 1) for case in cases]))
