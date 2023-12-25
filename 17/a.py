import heapq

g = dict()

with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]
    mx, my = len(ls[0]), len(ls)
    for _y, line in enumerate(ls):
        for _x, c in enumerate(line):
            g[(_x, _y)] = int(c)

dirs = [(+0, +1), (+1, +0), (-1, +0), (+0, -1)]


def search(start, goal, min_moves, max_moves):
    seen = set()
    todo = ([(0, start[0], start[1], 0, 0)])
    heapq.heapify(todo)

    while todo:
        cur_heat, x, y, from_x, from_y = heapq.heappop(todo)
        # print(f"looking @ {cur_heat, x, y, from_x, from_y}")
        if goal == (x, y):
            return cur_heat
        key = (x, y, from_x, from_y)
        if key in seen:
            continue
        seen.add(key)

        for (dx, dy) in dirs:
            step_heat, step_x, step_y = cur_heat, x, y
            if (dx, dy) == (from_x, from_y):  # can't go straight
                continue
            if (dx, dy) == (-from_x, -from_y):  # can't reverse
                continue

            for m in range(1, 1 + max_moves):
                step_x += dx
                step_y += dy
                if (step_x, step_y) in g:
                    step_heat += g[(step_x, step_y)]
                    if m >= min_moves:
                        # print(f"adding @ {step_heat, step_x, step_y, dx, dy}")
                        heapq.heappush(todo, (step_heat, step_x, step_y, dx, dy))
        # print("Done with iteration")


print(search((0, 0), (mx - 1, my - 1), 1, 3))
print(search((0, 0), (mx - 1, my - 1), 4, 10))
