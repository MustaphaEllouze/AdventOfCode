fic = open('input.txt','r')
lines = fic.readlines()
fic.close()

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
dic = {}
for i,let in enumerate(letters):
    dic[let] = i+1


# Partie 1
score = 0
for i,line in enumerate(lines):
    line_trait = line.strip()
    firstpart = line_trait[:int(len(line_trait)/2)]
    secondpart = line_trait[int(len(line_trait)/2):]
    common = []
    for char in firstpart:
        if char in secondpart and char not in common:
            common.append(char)
            score += dic[char]
print(score)

# Partie 2
score2 = 0
common = []
for i in range(int(len(lines)/3)):
    line_trait = lines[3*i].strip()
    line_trait2 = lines[3*i+1].strip()
    line_trait3 = lines[3*i+2].strip()
    
    l1 = set([c for c in line_trait])
    l2 = set([c for c in line_trait2])
    l3 = set([c for c in line_trait3])

    common += list(l1.intersection(l2).intersection(l3))

for c in common:
    score2 += dic[c]

print(score2)