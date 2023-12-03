with open('3_big') as fin:
    ls = [e.strip() for e in fin.readlines()]

parts, eng = list(), set()


def neigh(_x, _y, matching):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if abs(dx) + abs(dy) > 0:
                if (_x + dx, _y + dy) in matching:
                    return True
    return False


if __name__ == "__main__":
    for y, line in enumerate(ls):
        cur_part, spots = '', []
        for x, c in enumerate(line):
            if c in '0123456789':
                cur_part += c
                spots.append((x, y))
            else:
                if c != '.':
                    eng.add((x, y))
                if len(cur_part):
                    parts.append((int(cur_part), spots))
                cur_part, spots = '', []
        if cur_part:
            parts.append((int(cur_part), spots))

    total = 0
    for (value, spots) in parts:
        if any([neigh(*s, eng) for s in spots]):
            total += value
    print(total)
