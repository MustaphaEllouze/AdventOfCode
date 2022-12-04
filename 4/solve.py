fic = open('input.txt','r')
lines = fic.readlines()
fic.close()

score = 0
score2 = 0

for line in lines:
    a = line.strip().split(',')
    f_elf = [int(c) for c in a[0].split('-')]
    s_elf = [int(c) for c in a[1].split('-')]
    if((f_elf[0]>=s_elf[0] and f_elf[1]<=s_elf[1]) or (f_elf[0]<=s_elf[0] and f_elf[1]>=s_elf[1])):
        score += 1
    if(len(list(set(range(f_elf[0],f_elf[1]+1)).intersection(set(range(s_elf[0],s_elf[1]+1)))))!=0):
        score2 += 1

print(score,score2)
