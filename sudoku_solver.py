add = [0, 1, 2, 9, 10, 11, 18, 19, 20]


def check(a, p):
    row = [i for i in a[p-p % 9: p-p % 9+9] if i != 0]
    col = [i for i in [a[p % 9+9*i] for i in range(9)] if i != 0]
    first = ((p // 9) // 3)*27+((p % 9) // 3)*3
    cell = [first+i for i in add]
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
    if a[x[i]] == 9:
        a[x[i]] = 0
        i -= 1
    else:
        a[x[i]] += 1
        if check(a, x[i]):
            i += 1
    pp(a)
print('\n\n\n\n\n\n\n\n')
