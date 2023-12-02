import re # Para re-buscar o mesmo texto

def part1():
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # Valores que serão buscados
    soma = 0

    for x in f: # Para cada linha
        primeiro = True # True enquanto ainda não for encontrado um número
        for y in range(len(x)):
            if x[y] in nums: # Se achar um número...
                if primeiro: # Salva como primeiro dígito, se ainda não tiver achado um
                    n1 = x[y]
                    primeiro = False
                n2 = x[y] # Sempre salva como último dígito
        soma += int(n1 + n2) # Concatena String (primeiro e último dígito), converte para int e adiciona na soma
    print(soma)

def part2():
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # Valores que serão buscados
    soma = 0
    
    for x in f: # Para cada linha
        pos1 = -1 # -1 enquanto ainda não for encontrado um número
        pos2 = -1 # -1 enquanto ainda não for encontrado um número
        for n in nums: # Para cada opção da lista nums
            for m in re.finditer(n, x): # Encontra todas as ocorrências no texto e, para cada uma...
                pos = m.start() # Pega primeira posição do texto
                if pos != -1: # Se existir...
                    if pos1 == -1: # Se ainda não houver achado um dígito, salva como primeiro e último
                        n1 = n2 = n
                        pos1 = pos2 = pos
                    elif pos < pos1: # Se for antes do primeiro dígito salvo, substitui
                        n1 = n
                        pos1 = pos
                    elif pos > pos2: # Se for depois do último dígito salvo, substitui
                        n2 = n
                        pos2 = pos
        # END FOR
        # Se digito for um nome ["one" ~ "nine"], troca pela string do número ["1" ~ "9"]
        if n1 in nums[0:9]:
            n1 = str(nums.index(n1) + 1)
        if n2 in nums[0:9]:
            n2 = str(nums.index(n2) + 1)
        soma += int(n1 + n2) # Concatena String (primeiro e último dígito), converte para int e adiciona na soma
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