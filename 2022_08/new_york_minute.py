# Ryan Grayson
# Jane Street Puzzle August 2022
# New York Minute

grid = [
    "ytimoiczryzwbus",
    "tegcirbpylkoorb",
    "retpemplompilzy",
    "erhighlipetzxiz",
    "btmloisterslicp",
    "isstopestreetrk",
    "llteczerepzucze",
    "almeptrzlfzrkue",
    "oztbropxyoolegs",
    "ewjakoreztowpzt",
    "uigrzpcmeptrzlz",
    "ttzlmopeyislzpc",
    "zerzuqsposiczμi",
    "tlepputcpzllohu",
    "srzbzyypewnseuμ",
]

dim, tasks = len(grid), 0
in_a_task, edge_cases = set(), set()

# statueofliberty   z -> a, a -> f
for i in range(14, -1, -1):
    in_a_task.add((i, 0))
tasks += 1

# wallstreet
for i in range(9, -1, -1):
    in_a_task.add((i, 1))
tasks += 1

# taxi
for j in range(10, 14):
    in_a_task.add((3, j))
tasks += 1

# subway
for j in range(14, 8, -1):
    in_a_task.add((0, j))
tasks += 1
edge_cases.add((0, 9))

# brooklynbridge   p -> n, c -> d,  edge case y -> z back to y
for j in range(14, 0, -1):
    in_a_task.add((1, j))
tasks += 1
edge_cases.add((1, 8))

# cloisers   m -> c
for j in range(2, 11):
    in_a_task.add((4, j))
tasks += 1

# highline  
for j in range(2, 10):
    in_a_task.add((3, j))
tasks += 1

# radiocity    edge case y -> z back to y
for j in range(8, -1, -1):
    in_a_task.add((0, j))
tasks += 1
edge_cases.add((0, 0))

# stonestreet
for j in range(2, 13):
    in_a_task.add((5, j))
tasks += 1

# bronxzoo   y -> z
for j in range(3, 11):
    in_a_task.add((8, j))
tasks += 1

# centralpark   f -> p
for j in range(2, 13):
    in_a_task.add((7, j))
tasks += 1

# duanereade
for j in range(12, 2, -1):
    in_a_task.add((6, j))
tasks += 1

# laguardia
for i in range(10, 1, -1):
    in_a_task.add((i, 13))
tasks += 1

# grandcentral
for j in range(2, 14):
    in_a_task.add((10, j))
tasks += 1

# coneyisland    edge case y -> z back to y
for j in range(4, 15):
    in_a_task.add((11, j))
tasks += 1
edge_cases.add((11, 8))

# koreatown
for j in range(4, 13):
    in_a_task.add((9, j))
tasks += 1

# jfk
for j in range(2, 5):
    in_a_task.add((9, j))
tasks += 1

# lincolncenter
for j in range(12, -1, -1):
    in_a_task.add((2, j))
tasks += 1

# zabars
for j in range(5, -1, -1):
    in_a_task.add((14, j))
tasks += 1

# hollandtunnel
for j in range(13, 0, -1):
    in_a_task.add((13, j))
tasks += 1

# yankeestadium     μ -> m, edge case y -> z back to y
for i in range(2, 15):
    in_a_task.add((i, 14))
tasks += 1

edge_cases.add((2, 14))

# newμseum
for j in range(7, 15):
    in_a_task.add((14, j))
tasks += 1

# madisionsquare
for j in range(13, -1, -1):
    in_a_task.add((12, j))
tasks += 1

# one more edge case y -> z back to y
edge_cases.add((14, 6))

meeting_point = ''
replacement_grid = [[0] * dim for _ in range(dim)]

from termcolor import colored

print()
for i in range(15):
    for j in range(15):
        
        replaced = True
        char = grid[i][j]

        if char == 'z':
            char = 'a'
        elif char == 'a':
            char = 'f'
        elif char == 'p':
            char = 'n'
        elif char == 'c':
            char = 'd'
        elif char == 'm':
            char = 'c'
        elif char == 'y' and (i, j) not in edge_cases:
            char = 'z'
        elif char == 'f':
            char = 'p'
        elif char == 'μ':
            char = 'm'
        elif char == 'n':
            char = 'μ'
        else:
            replaced = False

        if char != 'μ' and (i, j) in in_a_task:
            char = char.capitalize()

        if replaced:
            replacement_grid[i][j] = colored(char, 'red')
        else:
            replacement_grid[i][j] = char

        if (i, j) not in in_a_task:
            char = colored(char, 'magenta')
            meeting_point += char
        elif (i, j) in edge_cases:
            char = colored(char, 'red')
        else:
            char = colored(char, 'green')

        print(char, end=' ')
    print()
print('\n' + colored('tasks: ' + str(tasks) + ' / 23', 'blue') + '\n')
print(colored('meeting point: ', 'cyan'), meeting_point + '\n')

# # maybe the replacements can reveal the 'why'?
# for row in replacement_grid:
#     for char in row:
#         print(char, end=' ')
#     print()
# print()
    
# # initial word search approach
# import enchant
# import queens_view
    
# english_words = enchant.Dict("en_US")
# words = []

# for i in range(dim):
#     for j in range(dim):
#         for r, c in queens_view(grid, i, j, 0, 0):
#             if abs(i - r) == 1 or abs(i - c)== 1:
#                 word = grid[r][c]
#             else:
#                 word += grid[r][c]

#             if english_words.check(word) and len(word) > 2:
#                 words.append(word)

# words.sort()
# for i in range(len(words)):
#     if i % 10 == 0:
#         print()
#     print(words[i], end='  ')
# print('\n')
