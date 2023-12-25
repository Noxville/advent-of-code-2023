with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]

dxy = {
    'R': (+1, +0),
    'L': (-1, +0),
    'D': (+0, +1),
    'U': (+0, -1)
}


def solve(lines, p2=False):
    x, y, vol, peri = 0, 0, 0, 0
    for ins, ln, col in [_.split(' ') for _ in lines]:
        if p2:
            ins, ln = 'RDLU'[int(col[-2])], int(col[-7:-2], 16)
        else:
            ins, ln = ins, int(ln)

        dx, dy = dxy[ins]
        next_x, next_y = x + (ln * dx), y + (ln * dy)
        vol += (x * next_y) - (y * next_x)
        x, y, peri = next_x, next_y, peri + ln
    print((abs(vol) // 2) + 1 + (peri // 2))


if __name__ == '__main__':
    solve(ls)
    solve(ls, p2=True)
