class Flow:
    @staticmethod
    def parse_rule(r):
        check, true = r.split(":")
        var, val = check.split("<") if '<' in check else check.split(">")
        sign = "<" if "<" in check else ">"
        return var, sign, int(val), true

    def __init__(self, s):
        left, right = s.split("{")
        self.name = left
        sp = right.replace("}", "").split(",")
        self.rules = []
        for i, li in enumerate(sp):
            if i == len(sp) - 1:
                self.default = li
            else:
                self.rules.append(self.parse_rule(li))

    def next_node(self, metal):
        for rule in self.rules:
            if eval(f"{metal.vars[rule[0]]} {rule[1]} {rule[2]}"):
                return rule[3]
        return self.default


class Metal:
    def __init__(self, s):
        self.vars = {}
        for _ in s.replace("{", '').replace("}", '').split(','):
            var, val = _.split('=')
            self.vars[var] = int(val)

    def rating(self):
        return sum([self.vars[_] for _ in 'xmas'])


with open('big') as fin:
    lines = fin.read().split('\n\n')
    flows = [Flow(e) for e in lines[0].split('\n')]

    flow_map = {f.name: f for f in flows}
    metals = [Metal(e) for e in lines[1].split('\n')]

    rating = 0
    for m in metals:
        f = flow_map['in']
        while True:
            nxt = f.next_node(m)
            if nxt == 'R':
                break
            elif nxt == 'A':
                rating += m.rating()
                break
            f = flow_map[nxt]
    print(rating)
