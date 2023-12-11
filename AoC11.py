def calc_lengths(part):
    dup_lin = [] # Vai guardar as linhas vazias
    dup_col = [] # Vai guardar as colunas vazias
    galaxies = [] # Vai guardar as posições das galáxias

    lines = f.splitlines()
    for idi, l in enumerate(lines): # Para cada linha
        empty_line = True
        for idj, c in enumerate(l): # Para cada char da linha
            if c == '#': # Se for uma galáxia, guarda a posição
                empty_line = False
                galaxies.append([idi, idj])
        if empty_line: # Se não achou nenhuma galáxia, guarda a posição da linha vazia
            dup_lin.append(idi)
    for idj in range(len(lines[0])): # Para cada coluna
        empty_col = True
        for idi in range(len(lines)): # Para cada char da coluna
            if lines[idi][idj] == '#': # Se achar alguma galáxia, para
                empty_col = False
                break
        if empty_col: # Se não achar nenhuma galáxia, salva a posição da coluna vazia
            dup_col.append(idj)
    
    dist = 0
    n = len(galaxies)
    for idi in range(n): # Para cada galáxia da lista
        for idj in range(idi+1,n): # Vai da seguinte até a última
            galaxies[idi]
            galaxies[idj]
            d = abs(galaxies[idi][0] - galaxies[idj][0]) + abs(galaxies[idi][1] - galaxies[idj][1]) # A distância entre elas será a soma das diferenças nas posições
            for dl in dup_lin: # Para cada linha vazia
                if galaxies[idi][0] < dl < galaxies[idj][0] or galaxies[idi][0] > dl > galaxies[idj][0]: # Se a linha estiver entre as posições das galáxias
                    if part == 1:
                        d += 1 # Adiciona 1 a distância (pois cada linha vazia deve ser dobrada e ela já foi contada uma vez)
                    else: # Parte 2
                        d += 999999 # Adiciona 999999 a distância (pois cada linha vazia deve valer 1000000 e ela já foi contada uma vez)
            for dc in dup_col: # Para cada coluna vazia
                if galaxies[idi][1] < dc < galaxies[idj][1] or galaxies[idi][1] > dc > galaxies[idj][1]: # Se a coluna estiver entre as posições das galáxias
                    if part == 1:
                        d += 1 # Adiciona 1 a distância (pois cada linha vazia deve ser dobrada e ela já foi contada uma vez)
                    else: # Parte 2
                        d += 999999 # Adiciona 999999 a distância (pois cada linha vazia deve valer 1000000 e ela já foi contada uma vez)
            dist += d # Soma a distância dessas duas galáxias ao total
    print(dist) # Resultado

def part1():
    calc_lengths(1)

def part2():
    calc_lengths(2)

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