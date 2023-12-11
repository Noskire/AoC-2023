import re # Para re-buscar o mesmo texto
from math import lcm

def part1():
    print("Part 1")
    lines = f.splitlines()
    print(lines)

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