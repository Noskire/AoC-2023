import re # Para re-buscar o mesmo texto

def validate_value(part, colors, min_values, set):
    # Ex. de entrada: "13 green"
    space = set.find(' ') # Encontra o espaço ' '
    num = int(set[0:space]) # O que tiver antes é o número
    name = set[space+1:len(set)] # O que tiver depois é o nome
    index = colors.index(name) # Pega a posição do nome na lista 'colors'

    if part == 1: # Parte 1 do desafio
        if num > (index + 12): # Verifica se o número é maior do que o máximo permitido
            # red (index 0) 12, green (index 1) 13 e blue (index 2) 14
            return True # Se for, o jogo será inválido
        return False
    else: # Parte 2 do desafio
        if num > min_values[index]: # Verifica se o número é maior do que o menor valor necessário até o momento
            min_values[index] = num # Atualiza mínimo

def line_to_sets(part, colors, line):
    # Ex. de entrada: "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    invalido = False # A princípio, todos os jogos são possíveis [Será usado na parte 1]
    min_values = [0, 0, 0] # Vai ser calculado o mínimo necessário para cada cor [Será usado na parte 2]

    start = line.find(':') + 2 # Ignora o início (Ex.: "Game 3: ")
    for m in re.finditer(';', line): # Encontra todas as ocorrências de ; no texto e, para cada uma...
        end = m.end() - 1 # Ignora o ;
        set = line[start:end] # Pega um conjunto de valores (Ex.: "5 blue, 4 red, 13 green")
        set = set + "," # Serve para demarcar o último conjunto
        
        start2 = 0 # A partir do início da string
        for v in re.finditer(',', set): # Encontra todas as ocorrências de , no texto e, para cada uma...
            end2 = v.end() - 1 # Ignora a ,
            if part == 1: # Parte 1 do desafio
                if validate_value(part, colors, 0, set[start2:end2]): # Valida valor [min_values será ignorado, portanto estou passando 0 ao invés da lista]
                    invalido = True
            else: # Parte 2 do desafio
                validate_value(part, colors, min_values, set[start2:end2]) # Calcula os mínimos
            start2 = end2 + 2 # Ajusta posição inicial, ignorando ", "
        
        start = end + 2 # Ajusta posição inicial, ignorando "; "
    if part == 1: # Parte 1 do desafio
        # Retorna True se algum dos valores for invalido
        return invalido
    else: # Parte 2 do desafio
        # Calcula a multiplicação dos valores na lista min_values
        power = 1 # Começa em 1 pois 1 * qualquer_coisa = qualquer_coisa
        for p in min_values:
            power *= p
        return power # Retorna total da multiplicação

def part1():
    colors = ["red", "green", "blue"]
    result = 0

    for line in f: # Para cada linha
        if line[len(line) - 1] == '\n': # Remove o \n, se houver
            line = line[0:len(line)-1]
        line = line + ";" # Serve para demarcar o último conjunto
        id = int(line[5:line.find(':')]) # Pega o id do jogo (O que estiver entre "Game " e ":")
        
        if not line_to_sets(1, colors, line): # Se for retornado False...
            result += id # Soma o id do jogo ao resultado
    print(result)

def part2():
    colors = ["red", "green", "blue"]
    result = 0

    for line in f: # Para cada linha
        if line[len(line) - 1] == '\n': # Remove o \n, se houver
            line = line[0:len(line)-1]
        line = line + ";" # Serve para demarcar o último conjunto
        
        result += line_to_sets(2, colors, line) # Soma o retorno da função ao resultado
    print(result)

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