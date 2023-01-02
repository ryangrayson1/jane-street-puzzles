import copy

global N, GRID, MOVES
N = 6
GRID = [
    [ 57,  33, 132, 268, 492, 732],
    [ 81, 123, 240, 443, 353, 508],
    [186,  42, 195, 704, 452, 228],
    [ -7,   2, 357, 452, 317, 395],
    [  5,  23,  -4, 592, 445, 620],
    [  0,  77,  32, 403, 337, 452]
]
MOVES = [('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1)]

class Die:
    def __init__(self, row = 5, col = 0):
        self.row = row
        self.col = col
        self.moves = 0
        self.steps = []
        self.score = 0
        self.seen = [[False] * N for _ in range(N)]
        self.T = None
        self.B = None
        self.L = None
        self.R = None
        self.U = None
        self.D = None

    def set_seen(self, val = True):
        self.seen[self.row][self.col] = val
    
    def set_next_top(self, move, val):
        if move == 'U' and self.D is None:
            self.D = val
        elif move == 'D' and self.U is None:
            self.U = val
        elif move == 'L' and self.R is None:
            self.R = val
        elif move == 'R' and self.L is None:
            self.L = val
        else:
            print("set_next_top() ERROR\n\n")

    def get_next_top(self, move):
        if move == 'U':
            return self.D
        if move == 'D':
            return self.U
        if move == 'L':
            return self.R
        if move == 'R':
            return self.L
        print("get_next_move() ERROR\n\n")

    def move(self, drctn):
        if drctn == 'U':
            self.row -= 1
            self.T, self.D, self.B, self.U = self.D, self.B, self.U, self.T
        elif drctn == 'D':
            self.row += 1
            self.T, self.U, self.B, self.D = self.U, self.B, self.D, self.T
        elif drctn == 'L':
            self.col -= 1
            self.T, self.R, self.B, self.L = self.R, self.B, self.L, self.T
        elif drctn == 'R':
            self.col += 1
            self.T, self.L, self.B, self.R = self.L, self.B, self.R, self.T
        else:
            print("move() ERROR\n\n")
            return
        
        self.moves += 1
        self.score += self.T * self.moves
    
    def p(self):
        print("position:", self.row, self.col)
        print("moves:", self.moves)
        print("score:", self.score)
        print("seen:")
        for r in self.seen:
            for c in r:
                print(1 if c else 0, end = ' ')
            print()
        print()
        print("         U:", self.U)
        print("      -----------")
        print("L:", self.L, "| T:", self.T, "B:", self.B, "| R:", self.R)
        print("      -----------")
        print("         D:", self.D)
        print("\n##################################################################\n")

def can_move(die, d, r, c):
    to_row, to_col = die.row + r, die.col + c
    if not (0 <= to_row < N and 0 <= to_col < N):
        return 0
    
    next_top = die.get_next_top(d)
    if next_top is None:
        if (GRID[die.row+r][die.col+c] - die.score) % (die.moves + 1):
            return 0
        return 1
    
    if die.score + next_top * (die.moves + 1) == GRID[to_row][to_col]:
        return 2
    
    return 0

global final_die
final_die = None

def backtrack(die):
    global final_die
    die.set_seen()
    die.steps.append((die.row, die.col))
    die.p()
    if die.row == 0 and die.col == 5:
        final_die = copy.deepcopy(die)
        return True

    for d, r, c in MOVES:
        print(d, r, c)
        can_mv = can_move(die, d, r, c)
        if can_mv > 0:
            nxt_die = copy.copy(die)

            if can_mv == 1:
                nxt_die.set_next_top(d, (GRID[die.row+r][die.col+c] - die.score) // (die.moves + 1))
            
            nxt_die.move(d)
            if backtrack(nxt_die):
                return True

    die.set_seen(False)
    die.steps.pop()
    return False

if not backtrack(Die()):
    print("No path found")
else:
    print("\nPATH FOUND!\n")
    print("steps taken:")
    print(*final_die.steps)
    print("final state:")
    final_die.p()
    ans = 0
    for row in range(N):
        for col in range(N):
            if not final_die.seen[row][col]:
                ans += GRID[row][col]
    
    print("******************")
    print("*  answer:", ans, " *")
    print("******************")
