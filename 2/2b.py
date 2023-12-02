with open('2_small') as fin:
    ls = [e.strip() for e in fin.readlines()]


def parse(s):
    sp = s.replace("Game ", "").split(":")
    num, games = int(sp[0]), sp[1].split(';')
    min_cols = {}
    for g in games:
        dice = g.strip().split(",")
        for die in dice:
            die = die.strip()
            count, color = int(die.split(' ')[0]), die.split(' ')[1][0]
            min_cols[color] = max(count, min_cols.get(color, 0))
    pwr = min_cols['r'] * min_cols['g'] * min_cols['b']
    return pwr


print(sum([parse(s) for s in ls]))
