import re # Para re-buscar o mesmo texto
from math import lcm

def part1():
    lines = f.splitlines()
    summarizing = 0

    a = 0
    b = 0
    while True:
        while lines[b] != '':
            b += 1
            if b >= len(lines):
                break
        pattern = lines[a:b]
        #print(pattern)
        # Testa reflexao na horizontal
        size = 0
        max_size = 0
        num_row = 0
        #print("Row")
        for idi in range(len(pattern)-1):
            #print(pattern[idi], pattern[idi+1])
            if pattern[idi] == pattern[idi+1]:
                #print("True")
                size = 1
                max_dist = min(idi, len(pattern)-idi-2)
                if max_dist == 0 and max_size == 0:
                    max_size = 1
                    num_row = idi + 1
                # if max_dist <= max_size:
                #     break
                for dist in range(1, max_dist+1):
                    if pattern[idi-dist] == pattern[idi+1+dist]:
                        size += 1
                        if dist == max_dist and size > max_size:
                            max_size = size
                            num_row = idi + 1
                    else:
                        if size > max_size:
                            max_size = size
                            num_row = idi + 1
        #print(num_row)

        # 'Rotaciona' lista
        rot_pattern = []
        for idj in range(len(pattern[0])):
            txt = ""
            for idi in range(len(pattern)):
                txt = txt + pattern[idi][idj]
            rot_pattern.append(txt)
        #print(rot_pattern)
        # Testa reflexao na vertical
        num_col = 0
        #print("Col")
        for idi in range(len(rot_pattern)-1):
            #print(rot_pattern[idi], rot_pattern[idi+1])
            if rot_pattern[idi] == rot_pattern[idi+1]:
                #print("True")
                size = 1
                max_dist = min(idi, len(rot_pattern)-idi-2)
                if max_dist == 0 and max_size == 0:
                    max_size = 1
                    num_col = idi + 1
                # if max_dist <= max_size:
                #     break
                for dist in range(1, max_dist+1):
                    if rot_pattern[idi-dist] == rot_pattern[idi+1+dist]:
                        size += 1
                        if dist == max_dist and size > max_size:
                            max_size = size
                            num_col = idi + 1
                    else:
                        if size > max_size:
                            max_size = size
                            num_col = idi + 1
        #print(num_col)

        if num_col == 0:
            summarizing += num_row * 100
        else:
            summarizing += num_col
        #print(num_col, num_row, summarizing)
        b += 1
        a = b
        if b >= len(lines):
            break
    print(summarizing)

def part2():
    print("Part 2")
    lines = f.splitlines()
    print(lines)

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