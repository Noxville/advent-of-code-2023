with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]


def hsh(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v = v % 256
    return v


if __name__ == '__main__':
    for line in ls:
        print(sum([hsh(bit) for bit in line.split(',')]))
