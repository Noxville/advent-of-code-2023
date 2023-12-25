from collections import defaultdict


def simulate_fall(pks, b):
    # x1, y1, z1, z2, y2, z2
    #  0   1   2   3   4   5
    spike = max(pks[(x, y)] for x in range(b[0], 1 + b[3]) for y in range(b[1], 1 + b[4]))
    cube_bottom = min(b[2], b[5])
    fall_dist = max(0, cube_bottom - spike - 1)
    return fall_dist, (b[0], b[1], b[2] - fall_dist, b[3], b[4], b[5] - fall_dist)


def tower_equilibrium(bricks):
    peaks = defaultdict(int)
    tower, fallen_bricks = [], 0
    for brick in bricks:
        dist, fallen_brick = simulate_fall(peaks, brick)
        fallen_bricks += 1 if dist > 0 else 0
        tower.append(fallen_brick)

        for x in range(fallen_brick[0], 1 + fallen_brick[3]):
            for y in range(fallen_brick[1], 1 + fallen_brick[4]):
                peaks[(x, y)] = max(fallen_brick[2], fallen_brick[5])

    return tower, fallen_bricks


if __name__ == "__main__":
    with open('big') as fin:
        ls = [e.strip() for e in fin.readlines()]
        _bricks = []
        for line in ls:
            c1, c2 = line.split("~")
            _bricks.append((list(map(int, c1.split(","))) + list(map(int, c2.split(",")))))
        _bricks = sorted(_bricks, key=lambda b: b[2])
    stable_tower, number_fallen = tower_equilibrium(_bricks)

    # test if stable when removing 1 at a time
    safely_removed, total_fallen = 0, 0
    for ex_idx in range(len(stable_tower)):
        other_bricks = [_ for idx, _ in enumerate(stable_tower) if idx != ex_idx]
        new_equilibrium, fallen = tower_equilibrium(other_bricks)
        if fallen == 0:
            safely_removed += 1
        else:
            total_fallen += fallen
    print(safely_removed)
    print(total_fallen)
