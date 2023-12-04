with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]

tot = 0
for line in ls:
    s = [_ for _ in line if _ in '0123456789']
    tot += int(s[0] + s[-1])
print(tot)
