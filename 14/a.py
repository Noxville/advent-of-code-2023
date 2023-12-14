roll, rock = set(), set()

with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]

    for y, line in enumerate(ls):
        for x, c in enumerate(line):
            if c == 'O':
                roll.add((x, y))
            elif c == '#':
                rock.add((x, y))


def tilt(rol, rok, dx, dy, dims):
    flag = True
    while flag:
        flag = False  # none have moved
        nxt = set()
        for r in sorted(list(rol), key=lambda xy: xy[0] * dx + xy[1] * dy):
            pos = (r[0] + dx, r[1] + dy)
            if pos not in nxt and pos not in rok and pos not in rol and 0 <= pos[0] < dims[0] and 0 <= pos[1] < dims[1]:
                nxt.add(pos)
                flag = True
            else:
                nxt.add(r)
        rol = nxt
        # prnt(rol, rok)
    return rol, rok


def north(rol, rok, dims):
    return load(tilt(rol, rok, 0, -1, dims)[0], dims)


def load(rol, dims):
    total = 0
    for _x in range(dims[0]):
        for _y in range(dims[1]):
            if (_x, _y) in rol:
                total += dims[1] - _y
    return total


def prnt(rol, rok, dims):
    for _y in range(dims[1]):
        lo = ''
        for _x in range(dims[0]):
            if (_x, _y) in rol:
                lo += 'O'
            elif (_x, _y) in rok:
                lo += '#'
            else:
                lo += '.'
        print(lo)
    print("")


if __name__ == "__main__":
    print(north(roll, rock, (len(ls[0]), len(ls))))
