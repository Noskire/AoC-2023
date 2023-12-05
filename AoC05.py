import re # Para re-buscar o mesmo texto

def str_to_array(array, txt):
    # Transforma uma string em um array de ints
    start = 0 # A partir do início da string
    for s in re.finditer(' ', txt): # Encontra todas as ocorrências de ' ' no texto e, para cada uma...
        end = s.end() - 1 # Ignora o ' '
        array.append(int(txt[start:end]))
        start = end + 1 # Ajusta posição inicial, ignorando o ' '

def range_to_array(array, txt):
    # Transforma uma string de intervalos em um array de ints
    n1 = -1
    start = 0 # A partir do início da string
    for s in re.finditer(' ', txt): # Encontra todas as ocorrências de ' ' no texto e, para cada uma...
        end = s.end() - 1 # Ignora o ' '
        if n1 == -1: # Se ainda não salvou o primeiro número do intervalo, salva
            n1 = int(txt[start:end])
        else: # Senão, salva o segundo e adiciona o intervalo na lista
            n2 = int(txt[start:end])
            array.append([n1, (n1+n2-1)])
            n1 = -1
        start = end + 1 # Ajusta posição inicial, ignorando o ' '

def convert_values(nums, maps):
    # Converte valor de acordo com intervalo
    for idx, n in enumerate(nums):
        for m in range(len(maps)//3):
            if n >= maps[m*3+1] and n <= (maps[m*3+1] + maps[m*3+2] - 1): # Se n estiver dentro do intervalo
                nums[idx] = maps[m*3] + (n - maps[m*3+1]) # Converte para novo valor
                break
            # Senão, mantém o mesmo valor

def convert_ranges(nums, maps, new_nums):
    for n in nums:
        no_match = True
        for m in range(len(maps)//3):
            if n[0] >= maps[m*3+1] and n[0] <= (maps[m*3+1] + maps[m*3+2] - 1): # Se o primeiro dígito do intervalo fonte (n[0]) estiver no intervalo alvo
                no_match = False # Encontrou uma correspondência
                if n[1] <= (maps[m*3+1] + maps[m*3+2] - 1): # Se o último dígito do intervalo fonte (n[1]) estiver no intervalo alvo
                    n0 = maps[m*3] + (n[0] - maps[m*3+1]) # Converte primeiro valor do intervalo
                    n1 = maps[m*3] + (n[1] - maps[m*3+1]) # Converte último valor do intervalo
                    new_nums.append([n0, n1]) # Adiciona novo intervalo na nova lista
                    break
                else: # Se o último dígito do intervalo fonte (n[1]) estiver ALÉM do intervalo alvo (não é possível ser menor, pois o primeiro valor já está dentro do intervalo)
                    n0 = maps[m*3] + (n[0] - maps[m*3+1]) # Converte primeiro valor do intervalo
                    n1 = maps[m*3] + maps[m*3+2] - 1 # Pega o último valor possível dentro do intervalo alvo
                    new_nums.append([n0, n1]) # Adiciona novo intervalo na nova lista

                    nums.append([n[0]+(n1-n0)+1, n[1]]) # Adiciona ao fim da lista fonte o restante do intervalo (trecho não convertido)
                    break
        if no_match: # Se não encontrar uma correspondência
            new_nums.append(n) # Adiciona intervalo na nova lista sem converter

def almanac(part): # Parte semelhante das duas partes
    nums = []
    maps = []
    new_nums = []
    stage = "seeds" # Separa a leitura da primeira linha das demais
    ignores = 2 # Ignora linha de 'estágio' (seed-to-soil map:) e linha vazia

    for line in f: # Para cada linha
        if line[len(line) - 1] == '\n': # Remove o \n, se houver
            line = line[0:len(line)-1]
        line = line + " " # Serve para demarcar o último conjunto

        if stage == "seeds": # Pega a lista de 'seeds'
            seeds = line[7:len(line)] # Ignora o início da string "seeds: "
            if part == 1:
                str_to_array(nums, seeds) # Converte string para uma lista de ints
            else: # Parte 2
                range_to_array(nums, seeds) # Converte string para uma lista de intervalos
            stage = "not seeds" # Termina leitura da primeira linha
        else: # Linhas de conversão
            if ignores > 0: # Ignora linha
                ignores -= 1
            else:
                if len(line) == 1: # Linha vazia com um espaço (por isso que == 1 ao invés de == 0)
                    if part == 1:
                        convert_values(nums, maps) # Converte valor de acordo com intervalo
                    else: # Parte 2
                        convert_ranges(nums, maps, new_nums) # Converte intervalos
                        nums.clear() # Limpa lista de intervalos
                        nums = new_nums.copy() # Copia a nova lista para a antiga
                        new_nums.clear() # Limpa a nova lista antes de começar o próximo estágio
                    ignores = 1 # Ignora a linha de 'estágio' seguinte "???-to-??? map:"
                    maps.clear() # Limpa lista de intervalos antes de começar o próximo estágio
                else: # Linha de valores
                    str_to_array(maps, line) # Salva intervalo na lista
    if part == 1:
        convert_values(nums, maps) # to_location (não tem linha vazia no final para entrar no IF acima)
        min = -1
        for n in nums: # Para todos os números, pega o menor
            if min == -1 or n < min:
                min = n
    else: # Parte 2
        convert_ranges(nums, maps, new_nums) # to_location (não tem linha vazia no final para entrar no IF acima)
        min = -1
        for n in new_nums: # Para todos os intervalos, pega o menor valor
            if min == -1 or n[0] < min: # Como todos os intervalos são crescentes, só é necessário testar o primeiro valor de cada
                min = n[0]
    return min

def part1():
    print(almanac(1))

def part2():
    print(almanac(2))

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