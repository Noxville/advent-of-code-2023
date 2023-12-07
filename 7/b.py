from collections import Counter

vals = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 1,
    'Q': 12,
    'K': 13,
    'A': 14
}


def score(hand):
    c = Counter(hand)
    freq = sorted(c.items(), key=lambda x: vals[x[0]], reverse=True)
    freq = sorted(freq, key=lambda x: x[1], reverse=True)
    tb = [vals[_[0]] for _ in hand]

    if hand == '':
        return [0, tb]
    if freq[0][1] == 5:
        return [7, tb]
    if freq[0][1] == 4:
        return [6, tb]
    if freq[0][1] == 3:
        if len(freq) >= 2 and freq[1][1] == 2:
            return [5, tb]
        else:
            return [4, tb]
    if freq[0][1] == 2:
        if len(freq) >= 2 and freq[1][1] == 2:
            return [3, tb]
        else:
            return [2, tb]
    return [1, tb]


def score_jokers(hand):
    raw, jokerless = score(hand), score(hand.replace('J', ''))
    jokers = hand.count('J')

    if jokers == 5:
        raw[0] = 7
    elif jokers == 4:
        raw[0] = 7
    elif jokers == 3:
        if jokerless[0] >= 2:
            raw[0] = 7
        else:
            raw[0] = 6
    elif jokers == 2:
        if jokerless[0] >= 4:
            raw[0] = 7
        elif jokerless[0] == 3:
            raw[0] = 6
        elif jokerless[0] == 2:
            raw[0] = 6
        elif jokerless[0] == 1:
            raw[0] = 4
    elif jokers == 1:
        if jokerless[0] == 6:
            raw[0] = 7
        elif jokerless[0] == 5:
            raw[0] = 6
        elif jokerless[0] == 4:
            raw[0] = 6
        elif jokerless[0] == 3:
            raw[0] = 5
        elif jokerless[0] == 2:
            raw[0] = 4
        if jokerless[0] == 1:
            raw[0] = 2

    return raw


with open('big') as fin:
    ls = [e.strip() for e in fin.readlines()]

    hands = []
    for l in ls:
        h, wager = l.split(" ")
        hands.append((score_jokers(h), h, wager))
    hands = sorted(hands)

    winnings = 0
    for idx, h in enumerate(hands):
        winnings += int(h[2]) * (1 + idx)
    print(winnings)
