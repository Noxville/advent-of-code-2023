class Node:
    def __init__(self, name, l, r):
        self.name = name
        self.l = l
        self.r = r


with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]
    ins, edg = ls[0], ls[2:]

edges = {}
for raw_e in edg:
    n_name, left, right = raw_e.replace(' = (', ',').replace(', ', ',').replace(')', '').split(',')
    edges[n_name] = Node(n_name, left, right)

idx, cur, steps = 0, edges['AAA'], 0
while True:
    if cur.name == 'ZZZ':
        print(steps)
        break

    cur = edges[cur.l] if ins[idx] == 'L' else edges[cur.r]
    idx = (1 + idx) % len(ins)
    steps += 1
