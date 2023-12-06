import re # Para re-buscar o mesmo texto

def str_to_array(array, txt):
    # Transforma uma string em um array de ints
    start = -1
    for idx, t in enumerate(txt):
        if t != " " and start == -1: # Pega a posição do primeiro número após o espaço
            start = idx
        elif t == " " and start != -1: # Pega a posição do último número antes do espaço
            end = idx
            array.append(int(txt[start:end])) # Salva valor em uma lista
            start = -1

def str_to_num(txt):
    # Transforma uma string em um único int
    num = ""
    start = -1
    for idx, t in enumerate(txt):
        if t != " " and start == -1: # Pega a posição do primeiro número após o espaço
            start = idx
        elif t == " " and start != -1: # Pega a posição do último número antes do espaço
            end = idx
            num = num + txt[start:end] # Concatena o valor na string
            start = -1
    return int(num)

def part1():
    time = []
    distance = []

    first_line = True
    for line in f: # Para cada linha
        if line[len(line) - 1] == '\n': # Remove o \n, se houver
            line = line[0:len(line)-1]
        line = line[9:len(line)] # Ignora o texto da string
        line = line + "  " # Serve para demarcar o último conjunto

        if first_line: # Se primeira linha, salva resultado na lista time
            str_to_array(time, line)
            first_line = False
        else: # Se segunda linha, salva resultado na lista distance
            str_to_array(distance, line)
    
    mult = 1
    for idx, t in enumerate(time):
        wins = 0
        for i in range(1, t+1): # Para cada milisegundo do tempo...
            mm = i * (t - i) # Calcular qual a distância percorrida ao soltar o botão neste momento
            if mm > distance[idx]: # Se for maior do que o recorde
                wins += 1 # Contabiliza
        mult *= wins # Multiplica as possibilidades de vitória
    print(mult)

def part2():
    time = ""
    distance = ""

    first_line = True
    for line in f: # Para cada linha
        if line[len(line) - 1] == '\n': # Remove o \n, se houver
            line = line[0:len(line)-1]
        line = line[9:len(line)] # Ignora o texto da string
        line = line + "  " # Serve para demarcar o último conjunto

        if first_line: # Se primeira linha, salva resultado na var time
            time = str_to_num(line)
            first_line = False
        else: # Se segunda linha, salva resultado na var distance
            distance = str_to_num(line)
    
    ways = 0
    first_win = -1
    last_win = -1
    for i in range(1, time+1): # Busca pelo primeiro milisegundo onde se obtém a vitória
        mm = i * (time - i)
        if mm > distance:
            first_win = i
            break
    for i in range(0, time): # Busca pelo último milisegundo onde se obtém a vitória
        mm = (time - i) * i
        if mm > distance:
            last_win = (time - i)
            break
    ways = last_win - first_win + 1 # O intervalo representa o número de possibilidades de vitórias possíveis
    print(ways)

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