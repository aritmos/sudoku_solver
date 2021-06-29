a = [int(i) for i in ' '.join([input() for _ in range(9)]).replace(' ', '')]
x = [i for i in filter(lambda n: a[n] == 0, range(81))]
i = 0
print('', end='\r\x1B[9A')
while i < len(x):
    if i < 0:
        print('\n\n\n\n\n\n\n\n\nERROR')
        quit()
    if a[x[i]] == 9:
        a[x[i]] = 0
        i -= 1
    else:
        a[x[i]] += 1
        row = [j for j in a[x[i]-x[i] % 9: x[i]-x[i] % 9+9] if j != 0]
        col = [j for j in [a[x[i] % 9+9*j] for j in range(9)] if j != 0]
        cell = [a[i] for i in [((x[i] // 9) // 3)*27+((x[i] % 9) // 3)*3 +
                j for j in [0, 1, 2, 9, 10, 11, 18, 19, 20]] if a[i] != 0]
        if all([len(set(j)) == len(j) for j in [row, col, cell]]):
            i += 1
    b = ' '.join([str(i) for i in a])
    for j in range(1, 9):
        b = b[:18*j-1] + '\n' + b[18*j:]
    print(b, end='\r\x1B[8A')
print('\n\n\n\n\n\n\n')
