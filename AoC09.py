def str_to_array(array, txt):
    # Transforma uma string em um array de ints
    if txt[len(txt) - 1] == '\n': # Remove o \n, se houver
        txt = txt[0:len(txt)-1]
    txt = txt + "  " # Serve para demarcar o último conjunto

    start = -1
    for idx, t in enumerate(txt):
        if t != " " and start == -1: # Pega a posição do primeiro número após o espaço
            start = idx
        elif t == " " and start != -1: # Pega a posição do último número antes do espaço
            end = idx
            array.append(int(txt[start:end])) # Salva valor em uma lista
            start = -1

def history_sequences(seq):
    # Gera sequências até que todos os números da sequência sejam 0
    all_zeros = False
    idx = 1 # Salva a posição da lista na matriz. 0 é a seq. inicial
    while not all_zeros: # Se pelo menos um dos número da última sequência não for zero
        all_zeros = True
        seq.append([]) # Cria uma nova lista na matriz
        for i in range(len(seq[idx-1])-1): # Para a quantidade de números da última sequência menos 1
            value = seq[idx-1][i+1] - seq[idx-1][i] # Calcula o valor seguinte menos o atual
            seq[idx].append(value) # Salva na nova lista
            if value != 0: # Se o valor não for zero, seta a flag como False
                all_zeros = False
        idx += 1 # Atualiza idx

def part1():
    sum = 0

    for line in f: # Para cada linha
        seq = [[]]
        str_to_array(seq[0], line)

        history_sequences(seq)
        
        value = 0
        for i in range(len(seq)): # Para cada sequência
            value += seq[i][len(seq[i])-1] # Soma o último valor
        sum += value # Soma todas as extrapolações
        seq.clear() # Reseta a lista seq para a próxima iteração
    print(sum)

def part2():
    sum = 0

    for line in f: # Para cada linha
        seq = [[]]
        str_to_array(seq[0], line)
        
        history_sequences(seq)

        value = 0
        for i in range(len(seq)): # Para cada sequência
            idx = len(seq) - 1 - i
            value = seq[idx][0] - value # Subtrai do primeiro valor a var value
        sum += value # Soma todas as extrapolações
        seq.clear() # Reseta a lista seq para a próxima iteração
    print(sum)

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