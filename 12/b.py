from functools import cache


def s_to_ints(s):
    return list(map(int, s.split(',')))


@cache
def count_valid(s, cts, length):
    # chomp from the front and lookup
    # print(f"s={s}, cts={cts}, ln={length}")

    cur, nxt = cts[0], cts[1:]
    remaining_chars = len(nxt) + sum(nxt)

    valid = 0
    for pre in range(1 + length - cur - remaining_chars):
        offset = cur + pre
        fine = True
        for c in s[pre:offset]:
            if c == '.':
                fine = False
        if fine:
            if not nxt:
                still_fine = True
                for c in s[offset:]:
                    if c == '#':
                        still_fine = False
                if still_fine:
                    valid += 1
            elif s[offset] != '#':
                valid += count_valid(s[offset + 1:], nxt, -1 + length - offset)
        if s[pre] == '#':
            break
    return valid


with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]

print(sum([count_valid("?".join((line.split()[0],) * 5),
                       tuple(s_to_ints(line.split()[1]) * 5),
                       len("?".join((line.split()[0],) * 5))) for line in ls]))
