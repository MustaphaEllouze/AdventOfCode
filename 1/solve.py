# 01-12-2022

# Parser
fic = open('input.txt','r')
lines = fic.readlines()
fic.close()

elves = []
elf = []

for line in lines:
    if line == '\n':
        elves.append(elf)
        elf = []
    else:
        elf.append(int(line.strip()))

# Calcul 
sum_elves = [sum(elf) for elf in elves]
sum_elves.sort()

# ----- Enigme 1 partie 1 -----
print('Answer Puzzle 1.1 = ' + str(sum_elves[-1]))

# ----- Enigme 2 partie 2 -----
print('Answer Puzzle 1.2 = ' + str(sum(sum_elves[-3:])))