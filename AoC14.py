def part1():
    lines = f.splitlines()
    load = 0
    for j in range(len(lines[0])):
        value = len(lines)
        for i in range(len(lines)):
            if lines[i][j] == 'O':
                load += value
                value -= 1
            elif lines[i][j] == '#':
                value = len(lines) - i - 1
    print(load)

def part2():
    lines = f.splitlines()
    grid = []
    for l in lines:
        grid.append(list(l))
    # for i in range(len(grid)):
    #     print(grid[i])
    for cycles in range(1000000000): # north, then west, then south, then east
        for j in range(len(grid[0])): # North
            pos = 0
            for i in range(len(grid)):
                if grid[i][j] == 'O':
                    if i != pos:
                        grid[pos][j] = 'O'
                        grid[i][j] = '.'
                    pos += 1
                elif grid[i][j] == '#':
                    pos = i + 1
        # print("NORTH")
        # for i in range(len(grid)):
        #     print(grid[i])
        for i in range(len(grid)): # West
            pos = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'O':
                    if j != pos:
                        grid[i][pos] = 'O'
                        grid[i][j] = '.'
                    pos += 1
                elif grid[i][j] == '#':
                    pos = j + 1
        # print("WEST")
        # for i in range(len(grid)):
        #     print(grid[i])
        for j in range(len(grid[0])): # South
            pos = len(grid) - 1
            for i in range(len(grid)):
                si = len(grid) - i - 1
                if grid[si][j] == 'O':
                    if si != pos:
                        grid[pos][j] = 'O'
                        grid[si][j] = '.'
                    pos -= 1
                elif grid[si][j] == '#':
                    pos = si - 1
        # print("SOUTH")
        # for i in range(len(grid)):
        #     print(grid[i])
        for i in range(len(grid)): # East
            pos = len(grid[0]) - 1
            for j in range(len(grid[0])):
                sj = len(grid[0]) - j - 1
                if grid[i][sj] == 'O':
                    if sj != pos:
                        grid[i][pos] = 'O'
                        grid[i][sj] = '.'
                    pos -= 1
                elif grid[i][sj] == '#':
                    pos = sj - 1
        # print("EAST")
        # for i in range(len(grid)):
        #     print(grid[i])
        print("END OF CYCLE", cycles,"/ 1000000000")
        # for i in range(len(grid)):
        #     print(grid[i])
        # if cycles == 1:
        #     break
        load = 0
        for j in range(len(grid[0])):
            value = len(grid)
            for i in range(len(grid)):
                if grid[i][j] == 'O':
                    load += value
                    value -= 1
                elif grid[i][j] == '#':
                    value = len(grid) - i - 1
        print(load)

# Escolhe se vai usar o arquivo test.txt ou input.txt como entrada
if input("1 - teste, 2 - input\n") == '1':
    file = open("test.txt", "r")
else:
    file = open("input.txt", "r")
f = file.read()

# Escolhe se vai resolver a parte 1 ou a parte 2 do desafio
if input("1 - part1, 2 - part2\n") == '1':
    part1()
else:
    part2()

file.close() # Fecha arquivo