def str_to_array(win_num, win_list):
    # Transforma a string de números vencedores em um array de ints
    index = 0
    while index < len(win_num):
        if win_num[index] == ' ': # Um dígito
            win_list.append(int(win_num[index+1]))
        else: # Dois dígitos
            win_list.append(int(win_num[index:index+2])) # +2 pq o último do intervalo é ignorado
        index += 3 # +3 pois pula dois caracteres e um espaço

def calc_pts(part, has_num, win_list):
    points = 0 # Qtd. de pts. do cartão
    # Pega número a número da string de números do jogo
    index = 0
    while index < len(has_num):
        if has_num[index] == ' ': # Um dígito
            value = int(has_num[index+1])
        else: # Dois dígitos
            value = int(has_num[index:index+2]) # +2 pq o último do intervalo é ignorado
        
        if value in win_list: # Se o número do jogo fizer parte dos números vendedores...
            if part == 1:
                if points == 0: # Se for o primeiro, pontua 1
                    points = 1
                else: # Senão, dobra a qtd. de pts.
                    points *= 2
            else: # Parte 2
                points += 1 # Pontua
        index += 3 # +3 pois pula dois caracteres e um espaço
    return points

def part1():
    soma = 0 # resultado
    for line in f: # Para cada linha
        if line[len(line) - 1] == '\n': # Remove o \n, se houver
            line = line[0:len(line)-1]
        win_num = line[line.find(':')+2:line.find('|')-1] # Vai pegar os números vencedores entre : e |
        has_num = line[line.find('|')+2:len(line)] # Vai pegar os números do jogo entre | e final da string
        win_list = []

        str_to_array(win_num, win_list)

        soma += calc_pts(1, has_num, win_list) # Soma os pts. do cartão ao total
    print(soma)

def part2():
    soma = 0
    total_lines = 189 ### Gambiarra, corrigir!
    cards = [1] * total_lines # Cria uma lista de tamanho igual ao número de linhas da entrada. A princípio, há 1 cartão de cada.

    idx = 0 # Salva o número do cartão/linha atual
    for line in f: # Para cada linha
        if line[len(line) - 1] == '\n': # Remove o \n, se houver
            line = line[0:len(line)-1]
        win_num = line[line.find(':')+2:line.find('|')-1] # Vai pegar os números vencedores entre : e |
        has_num = line[line.find('|')+2:len(line)] # Vai pegar os números do jogo entre | e final da string
        win_list = []

        str_to_array(win_num, win_list)
        
        points = calc_pts(2, has_num, win_list)
        for x in range(1, 1+points): # Para os próximos 'points' cartões...
            cards[idx + x] += cards[idx] # Adicionar a qtd. do cartão atual à qtd. do(s) próximo(s) cartão(ões)
        soma += cards[idx] # Soma a qtd. do cartão atual ao resultado
        idx += 1 # Atualiza o número do cartão/linha
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