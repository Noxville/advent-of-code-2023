EPSILON = 1.0 / (10 ** 7)
# MIN_XY, MAX_XY = 7, 27
MIN_XY, MAX_XY = 200000000000000, 400000000000000


def sign(fl):
    if abs(fl) <= EPSILON:
        return 0
    return 1 if fl > 0 else -1


class Hail:
    def __init__(self, s):
        sp = s.split(" @ ")
        self.x, self.y, self.z = map(int, list(map(str.strip, (sp[0].split(", ")))))
        self.dx, self.dy, self.dz = map(int, list(map(str.strip, (sp[1].split(", ")))))

    def __repr__(self):
        return f"{self.x, self.y, self.z} @ {self.dx, self.dy, self.dz}"

    def intersects(self, other):
        slope_us, slope_them = self.dy / self.dx, other.dy / other.dx
        intercept_us = self.y - (slope_us * self.x)
        intercept_them = other.y - (slope_them * other.x)

        if abs(slope_us - slope_them) <= EPSILON and abs(intercept_us - intercept_them):
            return 'PARA'
        if abs(slope_us - slope_them) <= EPSILON:
            return 'SAME'
        int_x = (intercept_them - intercept_us) / (slope_us - slope_them)
        int_y = intercept_us + (int_x * slope_us)

        yet_to_hit = sign(self.dx) == sign(int_x - self.x) and sign(other.dx) == sign(int_x - other.x)
        return 'INTERCEPT', int_x, int_y, yet_to_hit


if __name__ == "__main__":
    with open('big') as fin:
        hail = [Hail(e.strip()) for e in fin.readlines()]

        good = 0
        for i, a in enumerate(hail):
            for j, b in enumerate(hail):
                if j <= i:
                    continue

                ins = a.intersects(b)

                match ins[0]:
                    case 'PARA':
                        pass
                    case 'SAME':
                        good += 1
                    case 'INTERCEPT':
                        _, _x, _y, future = ins
                        if MIN_XY <= _x <= MAX_XY and MIN_XY <= _y <= MAX_XY and future:
                            good += 1

        print(good)
