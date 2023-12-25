from collections import defaultdict
from math import lcm


def part1(n_map):
    lo, hi = 0, 0
    state = {}

    G = defaultdict(list)

    # in-node dependencies
    for n_name, (n_type, to_nodes) in n_map.items():
        for to_node in to_nodes:
            G[to_node].append(n_name)

    # init state
    for n_name, (n_type, to_nodes) in n_map.items():
        match n_type:
            case 'BROADCASTER':
                pass
            case 'FLIP_FLOP':
                state[n_name] = False
            case 'CONJUNCTION':
                conj = {}
                for in_node in G[n_name]:
                    conj[in_node] = False
                state[n_name] = conj
            case _:
                raise Exception(n_type)

    for i in range(1000):
        Q = [('lo', 'broadcaster', None)]  # hi/lo, node, from

        while Q:
            next_gen_q = []

            for hilo, n_name, frm in Q:
                # print(f"MSG: {frm} -> {n_name} ({hilo})")
                if hilo == 'hi':
                    hi += 1
                elif hilo == 'lo':
                    lo += 1
                else:
                    raise Exception(f"hilo = {hilo}")

                if n_name not in n_map:
                    continue

                n_type, to_nodes = n_map[n_name]

                match n_type:
                    case 'BROADCASTER':
                        for to_node in to_nodes:
                            next_gen_q.append((hilo, to_node, n_name))
                    case 'FLIP_FLOP':
                        if hilo == 'lo':
                            for to_node in to_nodes:
                                next_gen_q.append(('lo' if state[n_name] else 'hi', to_node, n_name))
                            state[n_name] = not state[n_name]
                    case 'CONJUNCTION':
                        # print(f"STATE {state[n_name]}")
                        state[n_name][frm] = (hilo == 'hi')
                        propagate = 'hi' if [_ for _ in state[n_name].items() if not _[1]] else 'lo'
                        # print(f"conj state = {state[n_name]} prop=[{propagate}]")
                        for to_node in to_nodes:
                            next_gen_q.append((propagate, to_node, n_name))
                    case _:
                        raise Exception(n_type)

            Q = next_gen_q
    return hi * lo


def part2(n_map):
    state = {}

    G = defaultdict(list)

    # in-node dependencies
    for n_name, (n_type, to_nodes) in n_map.items():
        for to_node in to_nodes:
            G[to_node].append(n_name)

    # init state
    for n_name, (n_type, to_nodes) in n_map.items():
        match n_type:
            case 'BROADCASTER':
                pass
            case 'FLIP_FLOP':
                state[n_name] = False
            case 'CONJUNCTION':
                conj = {}
                for in_node in G[n_name]:
                    conj[in_node] = False
                state[n_name] = conj
            case _:
                raise Exception(n_type)

    # some hard-coded solutions are best
    in_sources = G['ll']
    cycle_len, cycles_counter = 0, {}

    while len(cycles_counter) != len(in_sources):

        cycle_len += 1

        Q = [('lo', 'broadcaster', None)]  # hi/lo, node, from

        while Q:
            next_gen_q = []

            for hilo, n_name, frm in Q:
                if n_name in in_sources and hilo == 'lo' and n_name not in cycles_counter:
                    cycles_counter[n_name] = cycle_len

                if n_name not in n_map:
                    continue

                n_type, to_nodes = n_map[n_name]

                match n_type:
                    case 'BROADCASTER':
                        for to_node in to_nodes:
                            next_gen_q.append((hilo, to_node, n_name))
                    case 'FLIP_FLOP':
                        if hilo == 'lo':
                            for to_node in to_nodes:
                                next_gen_q.append(('lo' if state[n_name] else 'hi', to_node, n_name))
                            state[n_name] = not state[n_name]
                    case 'CONJUNCTION':
                        state[n_name][frm] = (hilo == 'hi')
                        propagate = 'hi' if [_ for _ in state[n_name].items() if not _[1]] else 'lo'
                        for to_node in to_nodes:
                            next_gen_q.append((propagate, to_node, n_name))
                    case _:
                        raise Exception(n_type)

            Q = next_gen_q
    return lcm(*cycles_counter.values())


if __name__ == "__main__":
    nodes = {}
    with open('big') as fin:
        ls = [e.strip() for e in fin.readlines()]
        for line in ls:
            frm, to = line.split(" -> ")
            to_nodes = to.split(', ')
            match frm[0]:
                case 'b':
                    n_type = 'BROADCASTER'
                    name = 'broadcaster'
                case '%':
                    n_type = 'FLIP_FLOP'
                    name = frm[1:]
                case '&':
                    n_type = 'CONJUNCTION'
                    name = frm[1:]
            nodes[name] = (n_type, to_nodes)
    print(part1(nodes))
    print(part2(nodes))
