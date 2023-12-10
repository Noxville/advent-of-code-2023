from math import lcm
from a import Node


def c_steps(cur):
    idx, steps = 0, 0
    while True:
        if cur.name[-1] == 'Z':
            return steps

        cur = edges[cur.l] if ins[idx] == 'L' else edges[cur.r]
        idx = (1 + idx) % len(ins)
        steps += 1


with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]
    ins, edg = ls[0], ls[2:]

edges = {}
for raw_e in edg:
    n_name, left, right = raw_e.replace(' = (', ',').replace(', ', ',').replace(')', '').split(',')
    edges[n_name] = Node(n_name, left, right)

movers = [e for n, e in edges.items() if n[-1] == 'A']
tot = 1
for n in movers:
    tot = lcm(tot, c_steps(n))
print(tot)

