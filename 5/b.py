class NewMapper:
    def __init__(self, s):
        self.rules = list()

    def add_mapping_rule(self, vals):
        self.rules.append(vals)

    def apply(self, val):
        for to, frm, ln in self.rules:
            if frm <= val < ln + frm:  # + 1
                return val + to - frm
        return val


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlap(self, r2):
        ov = Range(max(r2.start, self.start), min(r2.end, self.end))
        if ov.start >= ov.end: 
            return None  # non-contig 
        return ov

    def shift(self, delta):
        return Range(delta + self.start, delta + self.end)

    def minus(self, r2):
        ov = self.overlap(r2)

        if ov is None:
            return [Range(self.start, self.end)]  # copy
        elif ov.start == self.start and ov.end == self.end:
            return []  # same
        elif ov.start == self.start:
            return [Range(ov.end, self.end)]  # merge
        elif ov.end == self.end:
            return [Range(self.start, ov.start)]  # merge
        else:
            return [Range(self.start, ov.start), Range(ov.end, self.end)]  # merge, merge


class TreeRangeTree:
    def __init__(self, mappers, max_depth):
        self.mappers = mappers
        self.max_depth = max_depth
        self.best = 10 ** 10

    def add_simple_guess(self, val):
        self.best = min(self.best, self.apply_mappers(val))

    def apply_mappers(self, val):
        for mp in self.mappers:
            val = mp.apply(val)
        return val

    def add_range(self, rng, depth):
        if depth == self.max_depth:
            self.best = min(self.best, rng.start)
            return
        for to, frm, ln in self.mappers[depth].rules:
            new_rng = Range(frm, ln + frm)
            ov = rng.overlap(new_rng)
            if ov is not None:
                self.add_range(ov.shift(to - frm), 1 + depth)
                diff = rng.minus(new_rng)
                if not diff:
                    return
                rng = diff[0]
                if len(diff) == 2:
                    self.add_range(diff[1], depth)
        self.add_range(rng, 1 + depth)  # we must go deeper


def chnk(ls, n):
    for i in range(0, len(ls), n):
        yield ls[i:i + n]


with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]

seed_rangelength = list(chnk(list(map(int, ls[0].replace("seeds: ", "").split(" "))), 2))

mps, cur = [], None
for line in ls[2:]:
    if 'map' in line:
        cur = NewMapper(line)
    elif not line:
        if cur:
            mps.append(cur)
    else:
        cur.add_mapping_rule(list(map(int, line.split(" "))))
mps.append(cur)

foo = TreeRangeTree(mps, len(mps))
for idx, (seed_range_start, range_length) in enumerate(seed_rangelength):
    foo.add_simple_guess(seed_range_start)  # the best answer might be the start of one of the first ranges
    foo.add_range(Range(seed_range_start, seed_range_start + range_length), 0)
print(foo.best)
