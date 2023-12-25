from functools import lru_cache

dxy = {
    '^': [(+0, -1)],
    '>': [(+1, +0)],
    '<': [(-1, +0)],
    'v': [(+0, +1)],
    '.': [(+1, +0), (-1, +0), (+0, +1), (+0, -1)],
}


@lru_cache
def get_neighbours(pos, gd, p2=False):
    ret = []
    (_x, _y) = pos
    # print(f"pos = {pos}, dxy@ = {gd[_y][_x]}")
    next_cell = '.' if p2 else gd[_y][_x]
    for dx, dy in dxy[next_cell]:
        nx, ny = _x + dx, _y + dy
        if 0 <= nx < len(gd[0]) and 0 <= ny < len(gd) and gd[ny][nx] in dxy:
            ret.append((nx, ny))
    return tuple(ret)


def to_graph(gd, starting_pos, p2=False):
    """Cull dead-ends since we must backtrack"""
    Q = [starting_pos]
    graph = {}
    seen = set()

    while Q:
        node = Q.pop()
        if node in seen:
            continue
        graph[node] = list()
        for move_next in get_neighbours(node, gd, p2):
            # print(f"From {node}, move next: {move_next}")
            dead_end = False
            edge_len = 1
            last = node
            location = move_next
            while True:
                neighbours = get_neighbours(location, gd, p2)
                if gd[location[1]][location[0]] in 'v<>^' and neighbours == [last]:
                    dead_end = True  # One way in
                    break
                if len(neighbours) != 2:
                    break  # not a bridge node
                for neigh in neighbours:
                    if neigh != last:
                        last = location
                        location = neigh
                        edge_len += 1
                        break
            if dead_end:
                continue
            graph[node].append((location, edge_len))
            Q.append(location)
        seen.add(node)
    return graph


def walk_lengths(graph, start_pos, target_pos):
    Q = [((1, 0), 0, set([start_pos]))]
    while Q:
        node, dist, seen = Q.pop()
        if target_pos == node:
            yield dist
            continue
        for nxt_node, edge_len in graph[node]:
            if nxt_node not in seen:
                Q.append((nxt_node, dist + edge_len, seen | {nxt_node}))


if __name__ == '__main__':
    with open('big') as fin:
        grid = tuple([e.strip() for e in fin.readlines()])
    target = len(grid[0]) - 2, len(grid) - 1

    # p1
    G = to_graph(grid, (1, 0))
    paths = [_ for _ in walk_lengths(G, (1, 0), target)]
    print(max(paths))

    # p2
    G = to_graph(grid, (1, 0), p2=True)
    paths = [_ for _ in walk_lengths(G, (1, 0), target)]
    print(max(paths))
