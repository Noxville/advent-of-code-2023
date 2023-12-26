from collections import defaultdict


def diff_sum(split_partite):
    total = 0
    best_delta = -10000
    best_delta_node = None
    for node in split_partite:
        delta = len(G[node] - split_partite)
        if delta > best_delta:
            best_delta = delta
            best_delta_node = node
        total += delta
    return total, best_delta_node


if __name__ == "__main__":
    G = defaultdict(set)

    with open('big') as fin:
        ls = [e.strip().split(":") for e in fin.readlines()]
        for i, js_str in ls:
            for j in [_ for _ in js_str.split(' ') if _ != '']:
                G[i].add(j)
                G[j].add(i)
    bipartite = set(G)

    while True:
        # greedily remove the most connected nodes until there's just 3 cross-partite connections left
        diff, cull = diff_sum(bipartite)
        # print(diff, cull)
        if diff == 3:
            break
        bipartite.remove(cull)
    print(len(bipartite) * (len(G) - len(bipartite)))
