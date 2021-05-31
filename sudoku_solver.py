cell_indices = [
    [0, 1, 2, 9, 10, 11, 18, 19, 20],
    [3, 4, 5, 12, 13, 14, 21, 22, 23],
    [6, 7, 8, 15, 16, 17, 24, 25, 26],
    [27, 28, 29, 36, 37, 38, 45, 46, 47],
    [30, 31, 32, 39, 40, 41, 48, 49, 50],
    [33, 34, 35, 42, 43, 44, 51, 52, 53],
    [54, 55, 56, 63, 64, 65, 72, 73, 74],
    [57, 58, 59, 66, 67, 68, 75, 76, 77],
    [60, 61, 62, 69, 70, 71, 78, 79, 80]]


def find_cell(p):
    for val in cell_indices:
        try:
            val.index(p)
            return val
        except:
            pass


def check(a, p):
    row = [i for i in a[p-p % 9: p-p % 9+9] if i != 0]
    col = [i for i in [a[p % 9+9*i] for i in range(9)] if i != 0]
    cell = [a[i] for i in find_cell(p) if a[i] != 0]
    checks = [row, col, cell]
    ans = [len(set(i)) == len(i) for i in checks]
    return all(ans)


def pp(a):
    a = ' '.join([str(i) for i in a])
    for i in range(1, 9):
        a = a[:18*i-1] + '\n' + a[18*i:]
    print(a, end='\r\x1B[8A')


print('')

a = [int(i) for i in ' '.join([input() for _ in range(9)]).replace(' ', '')]
x = [i for i in filter(lambda n: a[n] == 0, range(81))]

initial_checks = [10*i for i in range(9)] + [13, 16, 37, 43, 64, 67]

for i in initial_checks:
    if check(a, i) == False:
        print('  ERROR: Inititial Sudoku is not valid')
        quit()

i = 0
print('', end='\r\x1B[9A')

while i < len(x):
    if i < 0:
        print('  ERROR: Sudoku is not solvable')
        quit()
    pp(a)
    if a[x[i]] == 9:
        a[x[i]] = 0
        i -= 1
    else:
        a[x[i]] += 1
        if check(a, x[i]):
            i += 1
print('\n\n\n\n\n\n\n\n')
