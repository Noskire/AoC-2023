def check_adjacency(pos, symbols_pos): # Checa se o número e o símbolo são adjacentes
    # pos [line, i, j] Ex: [0, 5, 7] linha 0, do char 5 ao char 7
    # symbols_pos [line, i] Ex: [1, 3] linha 1, char 3
    diff = abs(pos[0] - symbols_pos[0]) # Diferença das linhas
    if diff == 1: # linha acima ou abaixo
        if symbols_pos[1] >= (pos[1] - 1) and symbols_pos[1] <= (pos[2] + 1): # Se símbolo estiver entre pos-1 e pos+1 é adjacente
            return True
    elif diff == 0: # mesma linha
        if symbols_pos[1] == (pos[1] - 1) or symbols_pos[1] == (pos[2] + 1): #Precisa estar ao lado Ex.: *123 ou 123*
            return True
    return False # linha não adjacente (diff > 1) ou símbolo não adjacente

def schematic(part, values, nums, pos, symbols_pos): # Separa as informações da entrada em diferentes listas
    line = 0
    for x in f: # Para cada linha
        if x[len(x) - 1] == '\n': # Remove o \n, se houver
            x = x[0:len(x)-1]
        counting = False
        for y in range(len(x)): # Para cada char
            if x[y] in values: # Se achar um número...
                if not counting: # Começa a contar
                    counting = True
                    pos.append([line, y, 0]) # Salva a linha e a pos inicial
                elif counting and y == len(x) - 1: # Se estiver contando e for o último char da linha, para de contar
                    counting = False
                    i = len(pos) - 1
                    pos[i][2] = y # Salva pos final (aqui não tem -1 pois é último char da linha, ainda está na pos do número e não na pos seguinte)
                    nums.append(x[pos[i][1]:pos[i][2]+1]) # Salva valor
            elif x[y] == '.': # Se achar um ponto
                if counting: # Se estiver contando, para de contar
                    counting = False
                    i = len(pos) - 1
                    pos[i][2] = y - 1 # Salva pos final
                    nums.append(x[pos[i][1]:pos[i][2]+1]) # Salva valor
            else: # Symbol
                if counting: # Se estiver contando, para de contar
                    counting = False
                    i = len(pos) - 1
                    pos[i][2] = y - 1 # Salva pos final
                    nums.append(x[pos[i][1]:pos[i][2]+1]) # Salva valor
                if part == 1:
                    symbols_pos.append([line, y]) # Salva a posição do símbolo
                else: # Parte 2
                    if x[y] == '*': # Salva a posição do símbolo se for *
                        symbols_pos.append([line, y]) # Salva a posição do símbolo
        line += 1 # Atualiza valor da linha atual

def part1():
    values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # Valores que serão buscados
    nums = [] # Vai guardar os valores Ex.: "114"
    pos = [] # Vai guardar as posições dos valores Ex.: [0, 5, 7] linha 0, do char 5 ao char 7
    symbols_pos = [] # Vai guardar a posição de cada símbolo Ex: [1, 3] linha 1, char 3
    soma = 0 # Resultado

    schematic(1, values, nums, pos, symbols_pos)

    for idx, n in enumerate(nums): # Para cada número...
        for s in symbols_pos: # Verificar se toca em algum dos símbolos
            if check_adjacency(pos[idx], s): # Se for adjacente à um, não precisa verificar os restantes (break)
                soma += int(n) # Soma o valor ao resultado
                break
    print(soma)

def part2():
    values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # Valores que serão buscados
    nums = [] # Vai guardar os valores Ex.: "114"
    pos = [] # Vai guardar as posições dos valores Ex.: [0, 5, 7] linha 0, do char 5 ao char 7
    symbols_pos = [] # Vai guardar a posição de cada símbolo Ex: [1, 3] linha 1, char 3
    soma = 0 # Resultado

    schematic(1, values, nums, pos, symbols_pos)

    for s in symbols_pos: # Para cada símbolo *...
        ratio = 1
        adjacent = 0
        for idx, n in enumerate(nums):  # Verifica (se) quais números são adjacentes à ele
            if check_adjacency(pos[idx], s): # Para cada número adjacente
                adjacent += 1 # Acrescenta 1 ao contador
                ratio *= int(n) # Multiplica o ratio pelo valor
        if adjacent == 2: # Se for adjacente à exatamente 2 números
            soma += ratio # Soma o ratio ao resultado
    print(soma)

# Escolhe se vai usar o arquivo test.txt ou input.txt como entrada
if input("1 - teste, 2 - input\n") == '1':
    f = open("test.txt", "r")
else:
    f = open("input.txt", "r")

# Escolhe se vai resolver a parte 1 ou a parte 2 do desafio
if input("1 - part1, 2 - part2\n") == '1':
    part1()
else:
    part2()

f.close() # Fecha arquivo