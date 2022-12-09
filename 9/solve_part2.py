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

ph0 = [int(gr/2),int(gr/2)]
ph1 = [int(gr/2),int(gr/2)]
ph2 = [int(gr/2),int(gr/2)]
ph3 = [int(gr/2),int(gr/2)]
ph4 = [int(gr/2),int(gr/2)]
ph5 = [int(gr/2),int(gr/2)]
ph6 = [int(gr/2),int(gr/2)]
ph7 = [int(gr/2),int(gr/2)]
ph8 = [int(gr/2),int(gr/2)]

pt = [int(gr/2),int(gr/2)]
grille[tuple(pt)] += 1111111111
passage[tuple(pt)] = 1

def where_to_go(posh,post):
    d_v = posh[0]-post[0]
    d_h = posh[1]-post[1]

    # Adjacent -> Bouge pas
    if(((d_v)**2+(d_h)**2)**0.5<1.5):
        return (0,0)
    else:
        return (np.sign(d_v),np.sign(d_h))


def move(g,direction,posh,post,marker=None,puissance_head=2,puissance_tail=1):
    # g : grille
    # direction : mouvement de head
    # posh : position head (int,int,)
    # post : position tail (int,int,)
    
    tamp_h = posh
    tamp_t = post
    g[tuple(tamp_h)] -= 10**(puissance_head-1)
    if(direction=='U'):
        tamp_h[0] -= 1
    elif(direction=='D'):
        tamp_h[0] += 1
    elif(direction=='R'):
        tamp_h[1] += 1
    elif(direction=='L'):
        tamp_h[1] -= 1
    g[tuple(tamp_h)] += 10**(puissance_head-1)
    g,tamp_h,tamp_t,marker = follow(g,tamp_h,tamp_t,marker=marker,puissance_head=puissance_head,puissance_tail=puissance_tail)

    return g,tamp_h,tamp_t,marker

def follow(g,posh,post,marker=None,puissance_head=2,puissance_tail=1):
    tamp_h = posh
    tamp_t = post
    g[tuple(tamp_t)] -= 10**(puissance_tail-1)
    vect = where_to_go(tamp_h,tamp_t)
    tamp_t[1] += vect[1]
    tamp_t[0] += vect[0]
    g[tuple(tamp_t)] += 10**(puissance_tail-1)
    if (not marker is None):
        marker[tuple(pt)]=1
    return g,tamp_h,tamp_t,marker

for line in lines:
    dir,step = line.strip().split()
    for i in range(int(step)):
        grille,ph0,ph1,a        =   move(grille,dir          ,ph0,ph1,puissance_head= 10, puissance_tail=9)
        grille,ph1,ph2,a        = follow(grille              ,ph1,ph2,puissance_head= 9, puissance_tail=8)
        grille,ph2,ph3,a        = follow(grille              ,ph2,ph3,puissance_head= 8, puissance_tail=7)
        grille,ph3,ph4,a        = follow(grille              ,ph3,ph4,puissance_head= 7, puissance_tail=6)
        grille,ph4,ph5,a        = follow(grille              ,ph4,ph5,puissance_head= 6, puissance_tail=5)
        grille,ph5,ph6,a        = follow(grille              ,ph5,ph6,puissance_head= 5, puissance_tail=4)
        grille,ph6,ph7,a        = follow(grille              ,ph6,ph7,puissance_head= 4, puissance_tail=3)
        grille,ph7,ph8,a        = follow(grille              ,ph7,ph8,puissance_head= 3, puissance_tail=2)
        grille,ph8,pt ,passage  = follow(grille              ,ph8,pt ,marker = passage, puissance_head=2, puissance_tail=1)
    

print(np.sum(passage))