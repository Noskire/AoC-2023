from math import lcm # Calcular o MMC

def part1():
    instructions = ""
    network = []
    LR = []

    for line in f: # Para cada linha
        if instructions == "":
            instructions = line[0:len(line)-1] # Remove o /n
        elif line == "\n": # Ignora a linha vazia
            pass
        else: # AAA = (BBB, CCC)
            pos = line[0:3]
            left = line[7:10]
            right = line[12:15]
            network.append(pos) # Pos vai ficar em uma lista diferente para facilitar na hora de buscar com o index
            LR.append([left, right]) # LR são os caminhos disponíveis
    
    camel = "AAA" # Posição inicial
    steps = 0
    while True: # While True pois pode ser necessário repetir a sequência de instruções várias vezes
        for i in instructions: # Para cada comando L ou R
            steps += 1 # Soma um ao número de passos
            # A var camel recebe o texto do caminho escolhido
            if i == 'L':
                camel = LR[network.index(camel)][0]
            else: # R
                camel = LR[network.index(camel)][1]
            if camel == "ZZZ": # Se for ZZZ, chegou ao destino, encerra o loop mesmo no meio da sequência de instruções
                break
        if camel == "ZZZ": # Se for ZZZ, chegou ao destino, encerra o loop
            break
    print(steps)

def part2():
    instructions = ""
    network = []
    LR = []
    camel_ghosts = []

    for line in f: # Para cada linha
        if instructions == "":
            instructions = line[0:len(line)-1] # Remove o /n
        elif line == "\n": # Ignora a linha vazia
            pass
        else: # AAA = (BBB, CCC)
            pos = line[0:3]
            left = line[7:10]
            right = line[12:15]
            network.append(pos) # Pos vai ficar em uma lista diferente para facilitar na hora de buscar com o index
            LR.append([left, right]) # LR são os caminhos disponíveis
            if pos[2] == 'A': # Salva todas as posições que terminam com A em uma nova lista
                camel_ghosts.append(pos)
    
    cycles = []
    for c in camel_ghosts: # Para cada posição inicial...
        camel = c # Posição inicial
        steps = 0
        while True: # While True pois pode ser necessário repetir a sequência de instruções várias vezes
            for i in instructions: # Para cada comando L ou R
                steps += 1 # Soma um ao número de passos
                # A var camel recebe o texto do caminho escolhido
                if i == 'L':
                    camel = LR[network.index(camel)][0]
                else: # R
                    camel = LR[network.index(camel)][1]
                if camel[2] == 'Z': # Se o caminho terminar com Z, chegou ao destino, encerra o loop mesmo no meio da sequência de instruções
                    break
            if camel[2] == 'Z': # Se o caminho terminar com Z, chegou ao destino, encerra o loop
                break
        cycles.append(steps) # Guarda o número de passos desse ciclo na lista
    # Levando em consideração que todos os caminhos são cíclicos, ou seja...
    # Se para chegar de A à Z levou 6 passos, então será possível chegar à Z com 6, 12, 18, 24... passos
    # Calcula-se o MMC de todos os valores salvos na lista cycles e esse será o número de passos necessários...
    # ...para que todas as posições iniciais cheguem às posições finais simultaneamente.
    steps = lcm(*cycles) # MMC
    print(steps)

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