from a import parse
with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]


if __name__ == "__main__":
    win_c = {1 + idx: look_ahead for (idx, look_ahead) in enumerate([parse(c) for c in ls])}

    total, todo = len(ls), list(range(1, 1 + len(ls)))
    while todo:
        cur = todo.pop()
        skip = win_c[cur]
        total += skip
        todo.extend(range(1 + cur, 1 + cur + skip))
    print(total)
