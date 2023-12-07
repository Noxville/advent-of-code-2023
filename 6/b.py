from a import race, nums

if __name__ == "__main__":
    with open('big') as fin:
        ls = [nums(e.strip().replace(" ", "").replace(":", " "))
              for e in fin.readlines()]
    print(race(ls[0][0], ls[1][0]))
