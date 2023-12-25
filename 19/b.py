with open('big') as fin:
    s = fin.read()

    flows, _ = s.split("\n\n")

    nodes = {}
    for line in flows.split("\n"):
        flow_name, raw_rules = line.split("{")
        flow_rules = []
        for rule in raw_rules.replace("}","").split(","):
            if ":" not in rule:
                flow_rules.append((None, rule))
            else:
                var, val = rule.split(":")
                flow_rules.append((var, val))
        nodes[flow_name] = flow_rules

xmas = {'x': 0, 'm': 1, 'a': 2, 's': 3}


def total(ins, range_list):
    if ins == "A":
        vol = 1
        for nxt in range_list:
            vol *= len(nxt)
        return vol
    elif ins == "R":
        return 0

    volume = 0
    input_node = nodes[ins]

    for (rule, nxt) in input_node:
        if rule is None:
            return total(nxt, range_list) + volume
        split_ranges = [[val for val in _] for _ in range_list]

        func, val, op = None, int(rule[2:]), rule[1]
        if op == '<':
            func = lambda x: x < val
            not_func = lambda x: x >= val
        elif op == '>':
            func = lambda x: x > val
            not_func = lambda x: x <= val
        else:
            raise Exception

        split_ranges[xmas[rule[0]]] = list(filter(func, split_ranges[xmas[rule[0]]]))
        range_list[xmas[rule[0]]] = list(filter(not_func, range_list[xmas[rule[0]]]))
        volume += total(nxt, split_ranges)
    return volume


print(total("in", [range(1, 4001), range(1, 4001), range(1, 4001), range(1, 4001)]))
