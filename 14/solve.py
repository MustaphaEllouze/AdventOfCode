import numpy as np

fic = open('input.txt','r')
#fic = open('input_t.txt','r')
lines = fic.readlines()
fic.close()

fic_out = open('solve.out','w')

partie2 = True

# ----------------------------------------- JE TRACE ------------------------------------
def trace():
    g = len(str(len(map)-1))
    ligne1 = ' '*(g)
    ligne2 = ' '*(g)
    ligne3 = ' '*(g)
    for i in range(minx,maxx+1):
        ligne1+=str(i)[0]
        ligne2+=str(i)[1]
        ligne3+=str(i)[2]

    fic_out.write(ligne1+'\n')
    fic_out.write(ligne2+'\n')
    fic_out.write(ligne3+'\n')

    for i,elem in enumerate(map):
        fic_out.write(str(i).zfill(len(str(len(map)-1))))
        for e in elem:
            fic_out.write(e)
        fic_out.write('\n')

# ----------------------------------------- CONSTRUCTION ------------------------------

sourcex = 500
sourcey = 0

treated = [ line.strip().split(' -> ') for line in lines]
treated2 = []

minx = 10000
maxx = sourcex
miny = sourcey
maxy = -1

for line in treated:
    sub_elem = []
    for elem in line :
        sub_elem.append([int(e) for e in elem.split(',')])
    treated2.append(sub_elem)

for line in treated2:
    for elem in line:
        minx = min(minx,elem[0])
        maxx = max(maxx,elem[0])
        miny = min(miny,elem[1])
        maxy = max(maxy,elem[1])

print(minx,maxx,miny,maxy)

if partie2:
    maxy += 2
    minx -= 200
    maxx += 200

map = np.array([['.']*(maxx-minx+1)]*(maxy-miny+1))

if partie2:
    map[maxy,:]='#'

map[sourcey-miny,sourcex-minx]='+'

for line in treated2:
    for i in range(len(line)-1):
        elem1 = line[i]
        elem2 = line[i+1]
        first1 = min(elem1[1]-miny,elem2[1]-miny)
        secon1 = max(elem1[1]-miny,elem2[1]-miny)
        first2 = min(elem1[0]-minx,elem2[0]-minx)
        secon2 = max(elem1[0]-minx,elem2[0]-minx)
        map[first1:secon1+1,first2:secon2+1]='#'

# ----------------------------------------- LE SABLE TOMBE ------------------------------

nb_grain = 30000
debug = False
combien = 0

while(combien!=nb_grain):
    combien+=1

    try : 
        pos_g_x = sourcex
        pos_g_y = sourcey
        if(map[pos_g_y-miny,pos_g_x-minx] == 'o') : 
            combien -= 1
            break
        map[pos_g_y-miny,pos_g_x-minx] = 'o'

        while(True):
            map[pos_g_y-miny,pos_g_x-minx] = '.'
            if(map[pos_g_y-miny+1,pos_g_x-minx]=='.'):      # En bas libre
                if debug : print('v')
                pos_g_y+=1
                map[pos_g_y-miny,pos_g_x-minx]='o'
            elif(map[pos_g_y-miny+1,pos_g_x-minx]=='#' or map[pos_g_y-miny+1,pos_g_x-minx]=='o'):       # En bas block
                if(map[pos_g_y-miny+1,pos_g_x-minx-1]=='.'):    # A gauche libre
                    if debug : print('v<')
                    pos_g_y+=1
                    pos_g_x-=1
                    map[pos_g_y-miny+1,pos_g_x-minx-1]=='o'
                elif(map[pos_g_y-miny+1,pos_g_x-minx-1]=='#' or map[pos_g_y-miny+1,pos_g_x-minx-1]=='o'):     # A gauche block
                    if(map[pos_g_y-miny+1,pos_g_x-minx+1]=='.'):    # A droite libre
                        if debug : print('v>')
                        pos_g_y+=1
                        pos_g_x+=1
                        map[pos_g_y-miny+1,pos_g_x-minx+1]=='o'
                    elif(map[pos_g_y-miny+1,pos_g_x-minx+1]=='#' or map[pos_g_y-miny+1,pos_g_x-minx+1]=='o'):     # A droite block
                        if debug : print('.')
                        map[pos_g_y-miny,pos_g_x-minx] = 'o'
                        break
    except:
        combien-=1
        break

trace()

print(combien)

