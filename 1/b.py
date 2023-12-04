import re

with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]

dig_map = {}
for idx, d in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
    dig_map[d] = 1 + idx
for d in '123456789':
    dig_map[d] = int(d)

tot = 0
for line in ls:
    locs = {}
    for num, idx in dig_map.items():
        locs[idx] = locs[idx] if idx in locs else set()

        for m in re.finditer(num, line):
            locs[idx].add(m.start())

    digs = sorted([(y, x) for (x, s) in locs.items() for y in s])
    tot += int(str(digs[0][1]) + str(digs[-1][1]))
print(tot)
