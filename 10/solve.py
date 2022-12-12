fic = open('input.txt')
lines = fic.readlines()
fic.close()

cycle = [0]
values = [1,1]
iter = 0

for line in lines:
    a = line.strip()
    iter += 1
    cycle.append(iter)
    values.append(values[-1])
    if('noop' in a):
        pass
    elif('addx' in a):
        iter += 1
        cycle.append(iter)
        values.append(values[-1]+int(a.split()[1]))

# Part 1
print(sum([values[i]*cycle[i] for i in [20,60,100,140,180,220]]))

# Part 2
sol = ''
for i in range(1,len(cycle)):
    value = values[i]
    if(value-1<=(i-1)%40<=value+1):
        sol += '#'
    else:
        sol += '.'
    if(i%40==0):
        print(sol)
        sol = ''
