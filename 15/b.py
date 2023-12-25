from a import hsh

with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]

hm = {}


def op(s):
    if '-' in s:
        label = s.replace('-', '')
        key = hsh(label)
        hm[key] = [_ for _ in hm.get(key, []) if _[0] != label]
    else:
        label, val = s.split('=')
        key = hsh(label)
        cur, found = hm.get(key, []), False
        for it in cur:
            if it[0] == label:
                it[1] = val
                found = True
        if not found:
            cur.append([label, val])
        hm[key] = cur


for line in ls:
    for bit in line.split(','):
        op(bit)
    tot = 0
    for box_num, lens_list in hm.items():
        for idx, lens in enumerate(lens_list):
            tot += (1 + box_num) * (1 + idx) * int(lens[1])
    print(tot)
