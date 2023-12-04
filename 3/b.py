from a import neigh

with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]

if __name__ == "__main__":
    parts, gears = list(), set()

    for y, line in enumerate(ls):
        cur_part, spots = '', []
        for x, c in enumerate(line):
            if c in '0123456789':
                cur_part += c
                spots.append((x, y))
            else:
                if c == '*':
                    gears.add((x, y))
                if len(cur_part):
                    parts.append((int(cur_part), spots))
                cur_part, spots = '', []
        if cur_part:
            parts.append((int(cur_part), spots))

    total, leftover_parts = 0, []
    for gear in gears:
        maybe_geared = []
        for (value, spots) in parts:
            if any([neigh(*s, [gear]) for s in spots]):
                maybe_geared.append((value, spots))
        if len(maybe_geared) == 2:
            total += maybe_geared[0][0] * maybe_geared[1][0]

    print(total)
