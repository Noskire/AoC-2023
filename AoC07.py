def define_type(labels):
    # Cria um array com a quantidade de cartas repetidas
    array = []
    for l in labels:
        if l > 0:
            array.append(l)
    array.sort(reverse=True) # Ordena do maior para menor

    hand_type = -1
    if array[0] == 5: # 5 of a kind (5)
        hand_type = 0
    elif array[0] == 4: # 4 of a kind (4/1)
        hand_type = 1
    elif array[0] == 3:
        if array[1] == 2: # Full House (3/2)
            hand_type = 2
        else: # 3 of a kind (3/1/1)
            hand_type = 3
    elif array[0] == 2:
        if array[1] == 2: # 2 pairs (2/2/1)
            hand_type = 4
        else: # 1 pair (2/1/1/1)
            hand_type = 5
    else: # High card (1/1/1/1/1)
        hand_type = 6
    
    return hand_type

def define_type_joker(labels):
    # Cria um array com a quantidade de cartas repetidas
    joker = 0
    array = []
    for idx, l in enumerate(labels):
        if idx == len(labels)-1:
            joker = l
        elif l > 0:
            array.append(l)
    if joker == 5: # Se tiver 5 jokers, adiciona na lista até então vazia
        array.append(5)
    else: # Senão...
        array.sort(reverse=True) # Ordena do maior para menor
        array[0] += joker # Adiciona o valor de jokers à repetição mais comum

    hand_type = -1
    if array[0] == 5: # 5 of a kind (5)
        hand_type = 0
    elif array[0] == 4: # 4 of a kind (4/1)
        hand_type = 1
    elif array[0] == 3:
        if array[1] == 2: # Full House (3/2)
            hand_type = 2
        else: # 3 of a kind (3/1/1)
            hand_type = 3
    elif array[0] == 2:
        if array[1] == 2: # 2 pairs (2/2/1)
            hand_type = 4
        else: # 1 pair (2/1/1/1)
            hand_type = 5
    else: # High card (1/1/1/1/1)
        hand_type = 6
    
    return hand_type

def sort_by_strength(cards, hands, types, bids):
    #for idx, t in enumerate(types):
    for idx in range(len(types)):
        i = idx
        for j in range(1, idx+1):
            if types[i] < types[idx-j]:
                # Update types
                aux = types[idx-j]
                types[idx-j] = types[i]
                types[i] = aux
                # Update bids
                aux = bids[idx-j]
                bids[idx-j] = bids[i]
                bids[i] = aux
                # Update hands
                aux = hands[idx-j]
                hands[idx-j] = hands[i]
                hands[i] = aux
                # Update pos
                i = idx-j
            elif types[i] == types[idx-j]:
                for k in range(0, 5):
                    if cards.index(hands[i][k]) < cards.index(hands[idx-j][k]):
                        aux = types[idx-j]
                        types[idx-j] = types[i]
                        types[i] = aux
                        # Update bids
                        aux = bids[idx-j]
                        bids[idx-j] = bids[i]
                        bids[i] = aux
                        # Update bids
                        aux = hands[idx-j]
                        hands[idx-j] = hands[i]
                        hands[i] = aux
                        # Update pos
                        i = idx-j
                        break
                    elif cards.index(hands[i][k]) > cards.index(hands[idx-j][k]):
                        break
                    # Se for igual, faz nada, vai para o próximo k
            else:
                break

def part1():
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] # Ranking das cartas
    hands = []
    bids = []
    types = []
    total_winnings = 0

    for line in f: # Para cada linha
        if line[len(line) - 1] == '\n': # Remove o \n, se houver
            line = line[0:len(line)-1]
        hands.append(line[0:5]) # Salva as 5 cartas
        bids.append(int(line[6:len(line)])) # Salva o valor da aposta
    for h in hands: # Para cada mão
        labels = [0] * 13
        for c in h: # Calcular o número de cada tipo de carta (A, K, Q...) presente na mão
            labels[cards.index(c)] += 1
        types.append(define_type(labels)) # Definir ranking da mão (0-5oak ~ 6-Highest)
    sort_by_strength(cards, hands, types, bids) # Ordenar listas por ranking

    tam = len(hands) # O tamanho da lista será igual ao multiplicador da melhor mão
    for idx, b in enumerate(bids):
        rank = tam - idx # Diminuir o idx do multiplicador
        total_winnings += rank * b # Multiplicar e somar ao total
    print(total_winnings)

def part2():
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']  # Ranking das cartas
    hands = []
    bids = []
    types = []
    total_winnings = 0

    for line in f: # Para cada linha
        if line[len(line) - 1] == '\n': # Remove o \n, se houver
            line = line[0:len(line)-1]
        hands.append(line[0:5]) # Salva as 5 cartas
        bids.append(int(line[6:len(line)])) # Salva o valor da aposta
    for h in hands: # Para cada mão
        labels = [0] * 13
        for c in h: # Calcular o número de cada tipo de carta (A, K, Q...) presente na mão
            labels[cards.index(c)] += 1
        types.append(define_type_joker(labels)) # Definir ranking da mão (0-5oak ~ 6-Highest)
    sort_by_strength(cards, hands, types, bids) # Ordenar listas por ranking

    tam = len(hands) # O tamanho da lista será igual ao multiplicador da melhor mão
    for idx, b in enumerate(bids):
        rank = tam - idx # Diminuir o idx do multiplicador
        total_winnings += rank * b # Multiplicar e somar ao total
    print(total_winnings)

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