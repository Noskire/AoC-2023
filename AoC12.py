def validate(arrangement, txt_match):
    txt = ""
    counting = False
    sharp_size = 0
    for a in arrangement:
        if a == '#':
            if counting:
                sharp_size += 1
            else:
                counting = True
                sharp_size = 1
        elif a == '.' and counting:
            counting = False
            txt = txt + str(sharp_size) + ','
    if counting:
        txt = txt + str(sharp_size)
    else:
        txt = txt[0:len(txt)-1] # Remove a última ,
    #print(arrangement, txt)
    if txt == txt_match:
        return 1
    else:
        return 0

def recursive(arrangement, txt_match):
    count = 0
    duplicate = False
    for idx, a in enumerate(arrangement):
        if a == '?':
            duplicate = True
            copy1 = arrangement.copy()
            copy1[idx] = '.'
            count += recursive(copy1, txt_match)
            copy2 = arrangement.copy()
            copy2[idx] = '#'
            count += recursive(copy2, txt_match)
            break
    if not duplicate: # No ?
        count += validate(arrangement, txt_match)
    return count

def part1():
    lines = f.splitlines()
    arrangements = 0
    for l in lines:
        arrangement = list(l[0:l.index(' ')])
        txt_match = l[l.index(' ')+1:len(l)]
        #print(arrangement, txt_match)
        arrangements += recursive(arrangement, txt_match)
    print(arrangements)

def part2():
    lines = f.splitlines()
    arrangements = 0
    value_1 = 0
    value_2 = 0
    value_3 = 0
    for l in lines:
        arrangement = list(l[0:l.index(' ')])
        txt_match = l[l.index(' ')+1:len(l)]
        #print(arrangement, txt_match)
        value_1 = recursive(arrangement, txt_match)
        # Adiciona uma interrogação ao início da lista e roda novamente
        if arrangement[len(arrangement)-1] == '#':
            value_2 = 1
        else:
            arrangement.insert(0, '?')
            value_2 = recursive(arrangement, txt_match)
        # Adiciona uma interrogação ao fim da lista e roda novamente
        if arrangement[len(arrangement)-1] == '#':
            value_2 = 1
        else:
            del arrangement[0]
            arrangement.append('?')
            value_3 = recursive(arrangement, txt_match)
        if value_2 >= value_3:
            arrangements += value_1 * value_2 * value_2 * value_2 * value_2
            #print((value_1 * value_2 * value_2 * value_2 * value_2), " - ", value_1, value_2)
        else:
            arrangements += value_1 * value_3 * value_3 * value_3 * value_3
            #print((value_1 * value_3 * value_3 * value_3 * value_3), " - ", value_1, value_3)
        
    print(arrangements)

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