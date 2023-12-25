g = dict()
with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]
    mx, my = len(ls[0]), len(ls)
    for _y, line in enumerate(ls):
        for _x, c in enumerate(line):
            if c != '.':
                g[(_x, _y)] = c


def pr(st):
    for _y in range(len(ls)):
        ll = ''
        for _x in range(len(ls[0])):
            ll += '#' if (_x, _y) in st else '.'
        print(ll)


neighbours = {
    None: {'e': 'e', 'w': 'w', 'n': 'n', 's': 's'},
    '-': {'e': 'e', 'w': 'w', 'n': 'we', 's': 'we'},
    '|': {'e': 'ns', 'w': 'ns', 'n': 'n', 's': 's'},
    '\\': {'e': 's', 'w': 'n', 'n': 'w', 's': 'e'},
    '/': {'e': 'n', 'w': 's', 'n': 'e', 's': 'w'},
}


def calc_beam(bm):
    seen = set()
    beams = [bm]
    while beams:
        pp = beams.pop()
        cur_x, cur_y, cur_dir = pp

        if pp in seen:
            continue
        seen.add((cur_x, cur_y, cur_dir))

        mir = g.get((cur_x, cur_y))
        for new_dir in neighbours[mir][cur_dir]:
            dx, dy = dxy[new_dir]
            new_x, new_y = cur_x + dx, cur_y + dy
            if 0 <= new_x < mx and 0 <= new_y < my:
                beams.append((new_x, new_y, new_dir))

    return len({(t[0], t[1]) for t in seen}) - 1


dxy = {
    'n': (+0, -1),
    's': (+0, +1),
    'e': (+1, +0),
    'w': (-1, +0)
}

if __name__ == "__main__":
    print(calc_beam((-1, 0, 'e')))

    best = 0
    for x in range(mx):
        best = max(best, calc_beam((x, -1, 's')))
        best = max(best, calc_beam((x, mx, 'n')))
    for y in range(my):
        best = max(best, calc_beam((-1, y, 'e')))
        best = max(best, calc_beam((my, y, 'w')))
    print(best)
