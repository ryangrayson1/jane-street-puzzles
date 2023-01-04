from math import gcd
from functools import cache

def order(a, b, c, d):
    if not a == b == c == d:
        mn = min(a, b, c, d)
        while a != mn or d == mn:
            a, b, c, d = d, a, b, c
        if b > d:
            b, d = d, b
    return a, b, c, d

@cache
def f(a, b, c, d):
    if a == b == c == d == 0:
        return 1
    return 1 + f(*order(abs(a-b), abs(b-c), abs(c-d), abs(d-a)))

def fp(a, b, c, d):
    while not a == b == c == d == 0:
        print(a, b, c, d)
        a, b, c, d = order(abs(a-b), abs(b-c), abs(c-d), abs(d-a))
    print(0, 0, 0, 0)

def max_squares(n):
    mx, cur_best = 1, set()
    for b in range(1, n+1):
        for c in range(b+1, n+1):
            for d in range(c+1, n+1):
                t = (0, b, c, d)
                squares = f(*t)
                if squares == mx:
                    cur_best.add(t)
                if squares > mx:
                    mx, s = squares, {t}
    min_sum = float('inf')
    ans = None
    for t in s:
        if sum(t) < min_sum:
            min_sum = sum(t)
            ans = t
    print("n:", n)
    print("max squares:", mx)
    print("min sum vars:", ans)
    fp(*order(*ans))
    print()

for n in [4, 9, 11, 13, 31, 37, 44, 105, 125, 149, 355]:
    max_squares(n)

print("\n------------------------------------------------")
print("n:", 10_000_000)
print("max squares:", 44)
print("min sum vars:", 0, 1389537, 3945294, 8646064)
fp(0, 1389537, 3945294, 8646064)
