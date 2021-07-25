

def battle(N, S, T):
    if N > 20 or N < 1:
        return "Out of Range"
    grid = [[0] * N for i in range(N)]
    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
    selected_grid = []
    i = 0
    for c in S.split(","):
        pos = []
        x = c.split()[0]
        y = c.split()[1]
        if x[0:-1] == y[0:-1]:
            for i in range(letter.index(x[-1]), letter.index(y[-1]) + 1):
                pos.append(x[0:-1] + letter[i])
        elif x[-1] == y[-1]:
            for i in range(int(x[0:-1]), int(y[0:-1]) + 1):
                pos.append(str(i) + x[-1])
        else:
            pos.append(x)
            pos.append(x[0:-1] + letter[letter.index(x[-1]) + 1])
            pos.append(str(int(x[0:-1]) + 1) + x[-1])
            pos.append(y)
        selected_grid.append(pos)
    hit = 0
    sunk = 0
    ls = T.split()
    for grid in selected_grid:
        grid_hit = 0
        for l in ls:
            for pt in grid:
                if pt == l:
                    grid_hit += 1
                    break
        if grid_hit == len(grid):
            sunk += 1
        elif grid_hit > 0:
            hit += 1
    ans = [str(sunk), str(hit)]
    return ",".join(ans)


S = "1B 2C 2D 4D"
T = "2B 2D 3D 4D 4A"
print(battle(3, S, T))
