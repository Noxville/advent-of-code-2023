from a import tilt, load

roll, rock = set(), set()
BIG = 1000000000

with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]

    for y, line in enumerate(ls):
        for x, c in enumerate(line):
            if c == 'O':
                roll.add((x, y))
            elif c == '#':
                rock.add((x, y))


def cycle(rol, rok, dims):
    rol, rok = tilt(rol, rok, +0, -1, dims)  # north 
    rol, rok = tilt(rol, rok, -1, +0, dims)  # west
    rol, rok = tilt(rol, rok, +0, +1, dims)  # south
    rol, rok = tilt(rol, rok, +1, +0, dims)  # east

    return rol, rok


if __name__ == "__main__":
    seen, dims, loads = dict(), (len(ls[0]), len(ls)), []
    cycle_start, cycle_length, left = None, None, None
    for i in range(BIG):
        roll, rock = cycle(roll, rock, dims)
        loads.append(load(roll, dims))
        ky = tuple(sorted(list(roll)))
        if ky in seen:
            #print(f"After {i} iterations we saw a configuration we last saw at {seen[ky]}")
            cycle_start, cycle_length, left = seen[ky], i - seen[ky], BIG - i
            break
        seen[ky] = i
    print(loads[(left % cycle_length) + cycle_start - 1])
