def part1():
    s_pos = []
    lines = f.splitlines()
    
    line_len = len(lines[0])
    for idl, l in enumerate(lines):
        new_line = ""
        for idx, x in enumerate(l):
            ### Se x for 'S' ou '.', mantém
            if x == '.' or x == 'S':
                new_line += x
                if x == 'S':
                    s_pos = [idl, idx]
            else: # Senão, valida cano
                ### Se cano puder se conectar nos dois caminhos, mantém
                ### Senão, não é possível fazer um loop com esse cano, o troca por um .
                N = False
                E = False
                S = False
                W = False
                invalid_pipe = False
                if x == '|':
                    N = True
                    S = True
                elif x == '-':
                    E = True
                    W = True
                elif x == 'L':
                    N = True
                    E = True
                elif x == 'J':
                    N = True
                    W = True
                elif x == '7':
                    S = True
                    W = True
                elif x == 'F':
                    S = True
                    E = True
                # Testa se há canos que podem se conectar nas direções marcadas acima
                if N and not invalid_pipe:
                    if idl == 0: # Não há linha acima
                        #lines[idl][idx] = '.'
                        new_line += '.'
                        invalid_pipe = True
                    elif lines[idl-1][idx] != 'S' and lines[idl-1][idx] != '|' and lines[idl-1][idx] != '7' and lines[idl-1][idx] != 'F': # Não é possível se conectar ao cano acima
                        new_line += '.'
                        invalid_pipe = True
                if S and not invalid_pipe:
                    if idl == len(lines)-1: # Não há linha abaixo
                        new_line += '.'
                        invalid_pipe = True
                    elif lines[idl+1][idx] != 'S' and lines[idl+1][idx] != '|' and lines[idl+1][idx] != 'L' and lines[idl+1][idx] != 'J': # Não é possível se conectar ao cano abaixo
                        new_line += '.'
                        invalid_pipe = True
                if E and not invalid_pipe:
                    if idx == line_len-1: # Não há cano a direita
                        new_line += '.'
                        invalid_pipe = True
                    elif lines[idl][idx+1] != 'S' and lines[idl][idx+1] != '-' and lines[idl][idx+1] != 'J' and lines[idl][idx+1] != '7': # Não é possível se conectar ao cano da direita
                        new_line += '.'
                        invalid_pipe = True
                if W and not invalid_pipe:
                    if idx == 0: # Não há cano a esquerda
                        new_line += '.'
                        invalid_pipe = True
                    elif new_line[idx-1] != 'S' and new_line[idx-1] != '-' and new_line[idx-1] != 'L' and new_line[idx-1] != 'F': # Não é possível se conectar ao cano da esquerda
                        new_line += '.'
                        invalid_pipe = True
                # Se não saiu até agora, salva o cano
                if not invalid_pipe:
                    new_line += x
        # END FOR x
        lines[idl] = new_line
    # END FOR l
    # Acha início do loop
    if s_pos[0] > 0 and (lines[s_pos[0]-1][s_pos[1]] == '|' or lines[s_pos[0]-1][s_pos[1]] == '7' or lines[s_pos[0]-1][s_pos[1]] == 'F'):
        pos = [s_pos[0]-1, s_pos[1]]
        dir = 'S'
    elif s_pos[0] < len(lines)-1 and (lines[s_pos[0]+1][s_pos[1]] == '|' or lines[s_pos[0]+1][s_pos[1]] == 'L' or lines[s_pos[0]+1][s_pos[1]] == 'J'):
        pos = [s_pos[0]+1, s_pos[1]]
        dir = 'N'
    elif s_pos[1] < line_len-1 and (lines[s_pos[0]][s_pos[1]+1] == '-' or lines[s_pos[0]][s_pos[1]+1] == '7' or lines[s_pos[0]][s_pos[1]+1] == 'J'):
        pos = [s_pos[0], s_pos[1]+1]
        dir = 'E'
    elif s_pos[1] < line_len-1 and (lines[s_pos[0]][s_pos[1]-1] == '-' or lines[s_pos[0]][s_pos[1]-1] == 'L' or lines[s_pos[0]][s_pos[1]-1] == 'F'):
        pos = [s_pos[0], s_pos[1]-1]
        dir = 'W'
    dist = 1 # Move e inicia dist como 1
    l = lines[pos[0]][pos[1]]
    ### Move pelo loop até voltar para o início 'S'
    while l != 'S':
        if l == '|':
            if dir == 'N':
                pos = [pos[0]+1, pos[1]]
                dir = 'N'
            else: # 'S'
                pos = [pos[0]-1, pos[1]]
                dir = 'S'
        elif l == '-':
            if dir == 'E':
                pos = [pos[0], pos[1]-1]
                dir = 'E'
            else: # 'W'
                pos = [pos[0], pos[1]+1]
                dir = 'W'
        elif l == 'L':
            if dir == 'N':
                pos = [pos[0], pos[1]+1]
                dir = 'W'
            else: # 'E'
                pos = [pos[0]-1, pos[1]]
                dir = 'S'
        elif l == 'J':
            if dir == 'N':
                pos = [pos[0], pos[1]-1]
                dir = 'E'
            else: # 'W'
                pos = [pos[0]-1, pos[1]]
                dir = 'S'
        elif l == '7':
            if dir == 'S':
                pos = [pos[0], pos[1]-1]
                dir = 'E'
            else: # 'W'
                pos = [pos[0]+1, pos[1]]
                dir = 'N'
        elif l == 'F':
            if dir == 'S':
                pos = [pos[0], pos[1]+1]
                dir = 'W'
            else: # 'E'
                pos = [pos[0]+1, pos[1]]
                dir = 'N'

        dist += 1
        l = lines[pos[0]][pos[1]]
    ### Quando fechar o loop, retornar metade do tamanho (ponto mais distante)
    print(dist // 2)

def part2():
    lines = f.splitlines()
    s_pos = []
    
    line_len = len(lines[0])
    for idl, l in enumerate(lines):
        new_line = ""
        for idx, x in enumerate(l):
            ### Se x for 'S' ou '.', mantém
            if x == '.' or x == 'S':
                new_line += x
                if x == 'S':
                    s_pos = [idl, idx]
            else: # Senão, valida cano
                ### Se cano puder se conectar nos dois caminhos, mantém
                ### Senão, não é possível fazer um loop com esse cano, o troca por um .
                N = False
                E = False
                S = False
                W = False
                invalid_pipe = False
                if x == '|':
                    N = True
                    S = True
                elif x == '-':
                    E = True
                    W = True
                elif x == 'L':
                    N = True
                    E = True
                elif x == 'J':
                    N = True
                    W = True
                elif x == '7':
                    S = True
                    W = True
                elif x == 'F':
                    S = True
                    E = True
                # Testa se há canos que podem se conectar nas direções marcadas acima
                if N and not invalid_pipe:
                    if idl == 0: # Não há linha acima
                        #lines[idl][idx] = '.'
                        new_line += '.'
                        invalid_pipe = True
                    elif lines[idl-1][idx] != 'S' and lines[idl-1][idx] != '|' and lines[idl-1][idx] != '7' and lines[idl-1][idx] != 'F': # Não é possível se conectar ao cano acima
                        new_line += '.'
                        invalid_pipe = True
                if S and not invalid_pipe:
                    if idl == len(lines)-1: # Não há linha abaixo
                        new_line += '.'
                        invalid_pipe = True
                    elif lines[idl+1][idx] != 'S' and lines[idl+1][idx] != '|' and lines[idl+1][idx] != 'L' and lines[idl+1][idx] != 'J': # Não é possível se conectar ao cano abaixo
                        new_line += '.'
                        invalid_pipe = True
                if E and not invalid_pipe:
                    if idx == line_len-1: # Não há cano a direita
                        new_line += '.'
                        invalid_pipe = True
                    elif lines[idl][idx+1] != 'S' and lines[idl][idx+1] != '-' and lines[idl][idx+1] != 'J' and lines[idl][idx+1] != '7': # Não é possível se conectar ao cano da direita
                        new_line += '.'
                        invalid_pipe = True
                if W and not invalid_pipe:
                    if idx == 0: # Não há cano a esquerda
                        new_line += '.'
                        invalid_pipe = True
                    elif new_line[idx-1] != 'S' and new_line[idx-1] != '-' and new_line[idx-1] != 'L' and new_line[idx-1] != 'F': # Não é possível se conectar ao cano da esquerda
                        new_line += '.'
                        invalid_pipe = True
                # Se não saiu até agora, salva o cano
                if not invalid_pipe:
                    new_line += x
        # END FOR x
        lines[idl] = new_line
    # END FOR l

    ### Acha peça que deve ser posta na posição inicial para fechar o Loop
    N = False
    E = False
    S = False
    W = False
    if s_pos[0] > 0 and (lines[s_pos[0]-1][s_pos[1]] == '|' or lines[s_pos[0]-1][s_pos[1]] == '7' or lines[s_pos[0]-1][s_pos[1]] == 'F'):
        N = True
    if s_pos[0] < len(lines)-1 and (lines[s_pos[0]+1][s_pos[1]] == '|' or lines[s_pos[0]+1][s_pos[1]] == 'L' or lines[s_pos[0]+1][s_pos[1]] == 'J'):
        S = True
    if s_pos[1] < line_len-1 and (lines[s_pos[0]][s_pos[1]+1] == '-' or lines[s_pos[0]][s_pos[1]+1] == '7' or lines[s_pos[0]][s_pos[1]+1] == 'J'):
        E = True
    if s_pos[1] > 0 and (lines[s_pos[0]][s_pos[1]-1] == '-' or lines[s_pos[0]][s_pos[1]-1] == 'L' or lines[s_pos[0]][s_pos[1]-1] == 'F'):
        W = True
    s_dir = ""
    if N and S: # |
        s_dir = '|'
    elif E and W: # -
        s_dir = '-'
    elif N and E: # L
        s_dir = 'L'
    elif N and W: # J
        s_dir = 'J'
    elif S and W: # 7
        s_dir = '7'
    elif S and E: # F
        s_dir = 'F'
    
    ### Acha início do loop
    if s_pos[0] > 0 and (lines[s_pos[0]-1][s_pos[1]] == '|' or lines[s_pos[0]-1][s_pos[1]] == '7' or lines[s_pos[0]-1][s_pos[1]] == 'F'):
        pos = [s_pos[0]-1, s_pos[1]]
        dir = 'S'
    elif s_pos[0] < len(lines)-1 and (lines[s_pos[0]+1][s_pos[1]] == '|' or lines[s_pos[0]+1][s_pos[1]] == 'L' or lines[s_pos[0]+1][s_pos[1]] == 'J'):
        pos = [s_pos[0]+1, s_pos[1]]
        dir = 'N'
    elif s_pos[1] < line_len-1 and (lines[s_pos[0]][s_pos[1]+1] == '-' or lines[s_pos[0]][s_pos[1]+1] == '7' or lines[s_pos[0]][s_pos[1]+1] == 'J'):
        pos = [s_pos[0], s_pos[1]+1]
        dir = 'E'
    elif s_pos[1] < line_len-1 and (lines[s_pos[0]][s_pos[1]-1] == '-' or lines[s_pos[0]][s_pos[1]-1] == 'L' or lines[s_pos[0]][s_pos[1]-1] == 'F'):
        pos = [s_pos[0], s_pos[1]-1]
        dir = 'W'
    
    ### Move pelo loop, trocando cada peça do loop por uma das direções (N, S, E ou W)
    l = lines[pos[0]][pos[1]]
    while l != 'S':
        last_pos = pos
        if l == '|':
            if dir == 'N':
                pos = [pos[0]+1, pos[1]]
                dir = 'N'
                nd = 'S'
            else: # 'S'
                pos = [pos[0]-1, pos[1]]
                dir = 'S'
                nd = 'N'
        elif l == '-':
            if dir == 'E':
                pos = [pos[0], pos[1]-1]
                dir = 'E'
                nd = 'W'
            else: # 'W'
                pos = [pos[0], pos[1]+1]
                dir = 'W'
                nd = 'E'
        elif l == 'L':
            if dir == 'N':
                pos = [pos[0], pos[1]+1]
                dir = 'W'
                nd = 'S'
            else: # 'E'
                pos = [pos[0]-1, pos[1]]
                dir = 'S'
                nd = 'N'
        elif l == 'J':
            if dir == 'N':
                pos = [pos[0], pos[1]-1]
                dir = 'E'
                nd = 'S'
            else: # 'W'
                pos = [pos[0]-1, pos[1]]
                dir = 'S'
                nd = 'N'
        elif l == '7':
            if dir == 'S':
                pos = [pos[0], pos[1]-1]
                dir = 'E'
                nd = 'N'
            else: # 'W'
                pos = [pos[0]+1, pos[1]]
                dir = 'N'
                nd = 'S'
        elif l == 'F':
            if dir == 'S':
                pos = [pos[0], pos[1]+1]
                dir = 'W'
                nd = 'N'
            else: # 'E'
                pos = [pos[0]+1, pos[1]]
                dir = 'N'
                nd = 'S'
        l = lines[pos[0]][pos[1]]
        lines[last_pos[0]] = lines[last_pos[0]][0:last_pos[1]] + nd + lines[last_pos[0]][(last_pos[1]+1):(len(lines[last_pos[0]]))]
    # END WHILE

    ### Substitui o S inicial por uma direção (N, S, E ou W)
    if s_dir == '|':
        if dir == 'N':
            nd = 'S'
        else: # 'S'
            nd = 'N'
    elif s_dir == '-':
        if dir == 'E':
            nd = 'W'
        else: # 'W'
            nd = 'E'
    elif s_dir == 'L':
        if dir == 'N':
            nd = 'S'
        else: # 'E'
            nd = 'N'
    elif s_dir == 'J':
        if dir == 'N':
            nd = 'S'
        else: # 'W'
            nd = 'N'
    elif s_dir == '7':
        if dir == 'S':
            nd = 'N'
        else: # 'W'
            nd = 'S'
    elif s_dir == 'F':
        if dir == 'S':
            nd = 'N'
        else: # 'E'
            nd = 'S'
    lines[s_pos[0]] = lines[s_pos[0]][0:s_pos[1]] + nd + lines[s_pos[0]][(s_pos[1]+1):(len(lines[s_pos[0]]))]

    ### Caso ainda haja peças (L, F, J, 7, | ou -), elas não fazem parte do loop. Troca por '.'
    for idl, l in enumerate(lines):
        new_line = ""
        for idx, x in enumerate(l):
            if x != 'N' and x != 'S' and x != 'W' and x != 'E':
                new_line += '.'
            else:
                new_line += x
        lines[idl] = new_line

    ### Todas as peças entre S~N ou N~S são consideradas estar dentro do loop
    ### Se alguma dessas peças for um '.', faz parte do possível ninho (nest)
    nest = 0
    for idl, l in enumerate(lines):
        in_loop = False
        dir = ""
        for idx, x in enumerate(l):
            if x == 'S' or x == 'N':
                if dir == "":
                    dir = x
                    in_loop = True
                elif dir != x:
                    in_loop = False
                else: # dir == x
                    in_loop = True
                #in_loop = not in_loop
            elif x == '.' and in_loop:
                lines[idl] = lines[idl][0:idx] + 'I' + lines[idl][(idx+1):(len(lines[idl]))]
                nest += 1
    print(nest)

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