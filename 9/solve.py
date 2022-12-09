import numpy as np

fic = open('input.txt','r')
lines = fic.readlines()
fic.close()

# taille grille
gr = 1000

# 
grille = np.zeros((gr,gr))
passage = np.zeros((gr,gr))

# Head = 10 ; Tail = 1

ph = [int(gr/2),int(gr/2)]
pt = [int(gr/2),int(gr/2)]
grille[tuple(pt)] += 1           
grille[tuple(ph)] += 10
passage[tuple(pt)] = 1

def where_to_go(posh,post):
    d_v = posh[0]-post[0]
    d_h = posh[1]-post[1]

    # Adjacent -> Bouge pas
    if(((d_v)**2+(d_h)**2)**0.5<1.5):
        return (0,0)
    else:
        return (np.sign(d_v),np.sign(d_h))


def move(g,direction,nstep,posh,post,marker):
    # g : grille
    # direction : mouvement de head
    # nstep : nombre de pas à faire
    # posh : position head (int,int,)
    # post : position tail (int,int,)
    
    tamp_h = posh
    tamp_t = post

    for i in range(nstep):
        g[tuple(tamp_h)] -= 10
        if(direction=='U'):
            tamp_h[0] -= 1
        elif(direction=='D'):
            tamp_h[0] += 1
        elif(direction=='R'):
            tamp_h[1] += 1
        elif(direction=='L'):
            tamp_h[1] -= 1
        g[tuple(tamp_h)] += 10
        g[tuple(tamp_t)] -= 1
        vect = where_to_go(tamp_h,tamp_t)
        tamp_t[1] += vect[1]
        tamp_t[0] += vect[0]
        g[tuple(tamp_t)] += 1
    
        marker[tuple(pt)]=1

    return g,tamp_h,tamp_t,marker

for line in lines:
    dir,step = line.strip().split()
    grille,ph,pt,passage = move(grille,dir,int(step),ph,pt,passage)

print(np.sum(passage))