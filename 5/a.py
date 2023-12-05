from rangetree import RangeTree


class Mapper:
    def __init__(self, ss):
        self.name = ss.replace(" map:", "")
        self.rt = RangeTree()

    def add_range(self, r):
        end, sta, ln = r
        self.rt[sta: sta + ln] = end - sta

    def conv(self, inp):
        if inp in self.rt:
            return self.rt[inp] + inp
        return inp

    def __repr__(self):
        return f"{self.name}"
    

if __name__ == "__main__":
    with open('big') as fin:
        ls = [e.strip() for e in fin.readlines()]

    initial_seeds = list(map(int, ls[0].replace("seeds: ", "").split(" ")))

    mps, cur = [], None
    for line in ls[2:]:
        if 'map' in line:
            cur = Mapper(line)
        elif not line:
            if cur:
                mps.append(cur)
        else:
            cur.add_range(list(map(int, line.split(" "))))
    mps.append(cur)
    
    best = 10**10
    for seed in initial_seeds:
        for mapper in mps:
            seed = mapper.conv(seed)
        best = min(best, seed)
    print(best)