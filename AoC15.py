def part1():
    lines = f.splitlines()
    sequence = lines[0].split(',')
    result = 0
    for s in sequence:
        hash_alg = 0
        for c in s:
            if c == '=':
                hash_alg += 61
            elif c == '-':
                hash_alg += 45
            elif c.isalpha():
                hash_alg += ord(c)
            elif c.isnumeric():
                hash_alg += ord(c)
            # else:
            #     print("Else: ", c)
            hash_alg = (hash_alg * 17) % 256
        result += hash_alg
    print(result)

def part2():
    lines = f.splitlines()
    sequence = lines[0].split(',')
    
    boxes = []
    for i in range(256):
        boxes.append([])
    
    for s in sequence:
        hash_alg = 0
        for idx, c in enumerate(s):
            if c.isalpha():
                hash_alg += ord(c)
            elif c.isnumeric():
                hash_alg += ord(c)
            elif c == '=':
                txt = s[0:idx]
                focal_len = s[len(s)-1]
                has_lens = False
                for b in boxes[hash_alg]:
                    if b[0] == txt:
                        has_lens = True
                        b[1] = focal_len
                        break
                if not has_lens:
                    boxes[hash_alg].append([txt, focal_len])
                break
            elif c == '-':
                txt = s[0:idx]
                has_lens = False
                for idj, b in enumerate(boxes[hash_alg]):
                    if b[0] == txt:
                        boxes[hash_alg].pop(idj)
                        break
                break
            hash_alg = (hash_alg * 17) % 256
    
        # for idx, b in enumerate(boxes):
        #     if len(b) > 0:
        #         print(idx, b)
        # print()
    
    result = 0
    for idx, b in enumerate(boxes):
        if len(b) > 0:
            for idj, s in enumerate(b):
                focusing_power = (idx+1) * (idj+1) * int(s[1])
                result += focusing_power
    print(result)

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