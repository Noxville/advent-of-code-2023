with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]


def parse(s):
    sp = s.replace("Game ", "").split(":")
    num, games = int(sp[0]), sp[1].split(';')
    for g in games:
        dice = g.strip().split(",")
        for die in dice:
            die = die.strip()
            count, color = int(die.split(' ')[0]), die.split(' ')[1]
            if color == 'red' and count > 12:
                return 0
            if color == 'green' and count > 13:
                return 0
            if color == 'blue' and count > 14:
                return 0
    return num


print(sum([parse(s) for s in ls]))
