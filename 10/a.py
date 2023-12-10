with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]

grid, start = dict(), (None, None)
for y, line in enumerate(ls):
    for x, c in enumerate(line):
        if c == '.':  pass
        else:
            grid[(x, y)] = c
            if c == 'S':
                start = (x, y)


def neighbours(n):
    _x, _y = n
    valid = {
        #    [L, R, U, D]
        'S': [1, 1, 1, 1],
        '.': [0, 0, 0, 0],
        '|': [0, 0, 1, 1],
        '-': [1, 1, 0, 0],
        'L': [0, 1, 1, 0],
        'J': [1, 0, 1, 0],
        '7': [1, 0, 0, 1],
        'F': [0, 1, 0, 1]
    }[grid[n]]
    neighs = []
    if valid[0] and (_x - 1, _y) in grid and grid[(_x - 1, _y)] in 'SFL-':
        neighs.append((_x - 1, _y))  # left
    if valid[1] and (_x + 1, _y) in grid and grid[(_x + 1, _y)] in 'S7J-':
        neighs.append((_x + 1, _y))  # right
    if valid[2] and (_x, _y - 1) in grid and grid[(_x, _y - 1)] in 'SF7|':
        neighs.append((_x, _y - 1))  # up
    if valid[3] and (_x, _y + 1) in grid and grid[(_x, _y + 1)] in 'SJL|':
        neighs.append((_x, _y + 1))  # down
    return neighs


dq = [(start, None)]
look_back = {}
while dq:
    cur, last = dq.pop()
    if last is not None and start == cur:
        break
    for neighbour in neighbours(cur):
        if last != neighbour:
            look_back[neighbour] = cur
            dq.append((neighbour, cur))

path = [start]
while True:
    cur = look_back[path[-1]]
    if start == cur:
        break
    path.append(cur)

print(len(path) // 2)
joined_path = path + [start]

double_volume = 0.0
for cur, nxt in zip(joined_path, joined_path[1:]):
    double_volume += cur[0] * nxt[1]
    double_volume -= cur[1] * nxt[0]

print(1.0 + (double_volume / 2) - (len(path) / 2))
