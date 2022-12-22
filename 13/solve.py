from functools import cmp_to_key

fic = open('input.txt','r')
#fic = open('input_t.txt','r')
lines = [eval(line.strip()) for line in fic.readlines() if line.strip()!='']
fic.close()

lines_ordered = [[lines[2*i],lines[2*i+1]] for i in range(len(lines)//2)]

part1 = False

def compare(a,b,donotreturn=False,printeur=False,depth = 0):
    if printeur : print('  '*depth + f'Comparing {a} and {b} :')
    if(type(a) in [float,int] and type(b) in [float,int]):
        if(a<b):
            if printeur : print('  '*depth + f'{a} is smaller than {b}')
            return 1
        elif(a==b):
            if printeur : print('  '*depth + f'{a} is equal to {b}')
            return 0
        else:
            if printeur : print('  '*depth + f'{a} is greater than {b}')
            return -1
    elif(type(a) is list and type(b) is list):
        lena = len(a)
        lenb = len(b)
        for i in range(min(lena,lenb)):
            test = compare(a[i],b[i],printeur=printeur,depth=depth+1)
            if (test in [-1,1]):
                return test
            else:
                continue
        if(not donotreturn):
            if(lena<lenb):
                if printeur : print('  '*depth + 'Left side ran out of items')
                return 1
            elif(lena>lenb):
                if printeur : print('  '*depth + 'Right side ran out of items')
                return -1
            else:
                if printeur : print('  '*depth + 'Lists are equal')
                return 0
    else:
        if (not type(a) is list) : a = [a]
        else                     : b = [b]
        test = compare(a,b,donotreturn=False,printeur=printeur,depth=depth+1)
        return test

if part1:
    score = 0
    for i,paire in enumerate(lines_ordered):
        print(f'--------------Paire {i}------------')
        print(f'--------------Paire {i}------------')
        print(f'--------------Paire {i}------------')
        t1 = paire[0]
        t2 = paire[1]
        print(t1)
        print(t2)
        test = compare(t1,t2,printeur=True)
        if (t1!=[[2]] and t2!=[[6]]):
            if(test==1):  
                score += (i+1)
                print('Right order')
            elif(test==0):
                raise Exception()
            else:
                print('Wrong order')
    
    print(score)

else : 
    lines = sorted(lines,key=cmp_to_key(compare),reverse=True)
    a = (lines.index([[2]]))
    b = (lines.index([[6]]))
    for elem in lines : print(elem)
    print(a,b)
    print((a+1)*(b+1))