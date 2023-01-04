# Ryan Grayson
# Jan 2023 Jane Street Puzzle


def next_seq(cur):
    nxt = []
    ta, tb, tc, td = cur[0]
    double = (td - tc - tb) % 2 == 1

    if double:
        tb, tc, td = tb*2, tc*2, td*2

    x = (td - tc - tb) // 2

    a1, b1, c1, d1 = ta+x, tb+x, tc+x, td+x
    a0, b0, c0, d0 = 0, a1, a1+b1, d1

    nxt.append((a0, b0, c0, d0))
    nxt.append((a1, b1, c1, d1))

    for a, b, c, d in cur[1:]:
        if double:
            nxt.append((a*2, b*2, c*2, d*2))
        else:
            nxt.append((a, b, c, d))

    return nxt

N = 10_000_000
# Best sequence where max value <= 4
cur = [
    (0, 1, 2, 4),
    (1, 1, 2, 4),
    (0, 1, 2, 3),
    (1, 1, 1, 3),
    (0, 0, 2, 2),
    (0, 2, 0, 2),
    (2, 2, 2, 2),
    (0, 0, 0, 0),
]
ans = None
while cur[0][3] <= N:
    ans = cur[0]
    for t in cur:
        print(t)
    print()
    cur = next_seq(cur)

print("********************************************")
print("* answer: ", ans, " *")
print("********************************************")
