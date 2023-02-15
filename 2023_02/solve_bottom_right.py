br = [[0] * 5 for _ in range(5)]
to_place = [0, 1, 0, 1, 2, 2, 4, 2]
row_needed = [2, 3, 2, 3, 2]
col_needed = [2, 3, 2, 3, 2]
row_sums = [12, 5, 9, 4, 10]
col_sums = [13, 3, 13, 2, 9]

def print_state():
    for r in br:
        print(*r)
    print()
    print("row_sums", row_sums)
    print()
    print("col_sums", col_sums)
    print()
    print("to_place", to_place)
    print()
    print("row_needed", row_needed)
    print()
    print("col_needed", col_needed)
    print()

def up(row, col, x):
    br[row][col] = x
    to_place[x] -= 1
    row_needed[row] -= 1
    col_needed[col] -= 1
    row_sums[row] += x
    col_sums[col] += x


def dn(row, col, x):
    br[row][col] = 0
    to_place[x] += 1
    row_needed[row] += 1
    col_needed[col] += 1
    row_sums[row] -= x
    col_sums[col] -= x

def valid_placement(row, col, x):
    if to_place[x] == 0:
        return False
    if row_sums[row] + x > 20:
        return False
    if col_sums[col] + x > 20:
        return False
    if row_needed[row] == 0:
        return False
    if col_needed[col] == 0:
        return False
    if row_needed[row] == 1 and row_sums[row] + x < 20:
        return False
    if col_needed[col] == 1 and col_sums[col] + x < 20:
        return False
    return True

def valid_grid():
    if sum(to_place) != 0:
        return False
    if sum(row_needed) != 0:
        return False
    if sum(col_needed) != 0:
        return False
    if row_sums.count(20) != 5:
        return False
    if col_sums.count(20) != 5:
        return False
    return True
    
def place(row, col):
    if row == col == 3:
        if valid_grid():
            print_state()
        return
    
    next_col = col + 1 if col < 3 else 0
    next_row = row + 1 if next_col == 0 else row

    place(next_row, next_col) # skip this cell
    for x in range(1, 8):
        if valid_placement(row, col, x):
            up(row, col, x)
            place(next_row, next_col)
            dn(row, col, x)

# initial cases to optimize
for b7c in [1, 3]:
    up(4, b7c, 7)
    for b3c in range(b7c):
        up(4, b3c, 3)
        for r5r in range(4):
            up(r5r, 4, 5)
            for r6r in range(r5r):
                up(r6r, 4, 6)
                place(0, 0)
                dn(r6r, 4, 6)
            dn(r5r, 4, 5)
        dn(4, b3c, 3)
    dn(4, b7c, 7)
