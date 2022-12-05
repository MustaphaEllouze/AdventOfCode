import numpy as np
fic = open('input.txt','r')
lines = fic.readlines()
fic.close()

crates = []
arrangements = []
flag_part2 = False

etape1 = False

for i,line in enumerate(lines):
    if(not flag_part2 and '1' not in line):
        lt = line[:-1]
        to_append = [lt[1+4*i] for i in range(len(line)//4)]
        crates.append(to_append)
    elif(not flag_part2):
        numbers = line.strip().split()
        flag_part2 = True
    elif(line!='\n'):
        line_trait = line.strip().split()
        arrangements.append((line_trait[1],line_trait[3],line_trait[5]))

# Transpose crates

crate_t = [[elem for elem in list(line)[::-1] if elem!=' '] for line in np.array(crates).T]

# BDD
crates_columns = {numbers[i] : crate_t[i] for i in range(len(numbers))}


# Arrangements :
for num,col1,col2 in arrangements:
    recup_col1 = crates_columns[col1]
    enleve = recup_col1[-int(num):]
    crates_columns[col1] = recup_col1[:-int(num)]
    if(etape1):
        crates_columns[col2] += enleve[::-1]
    else:
        crates_columns[col2] += enleve

# Solution
sol = ''
for num in numbers:
    sol += crates_columns[num][-1]

print(sol)