import numpy as np

fic = open('input.txt','r')
lines = fic.readlines()
fic.close()

lines_trait = [list(line.strip()) for line in lines]

forest = np.array(lines_trait,dtype=int)
cache = np.zeros(np.shape(forest))
score = np.zeros(np.shape(forest))

for i in range(np.shape(forest)[0]):
    for j in range(np.shape(forest)[1]):
        haut =     np.any(forest[0:i,j]  >= forest[i,j])
        bas =      np.any(forest[i+1:,j] >= forest[i,j])
        gauche =   np.any(forest[i,0:j]  >= forest[i,j])
        droite =   np.any(forest[i,j+1:] >= forest[i,j])
        cache[i,j] = float(haut and bas and gauche and droite)

print(np.sum(1-cache))

def view_score(liste,foret):
    rang = 0
    for tree in liste:
        rang+= 1
        if(tree>=foret[i,j]):
            return rang
    return rang

for i in range(np.shape(forest)[0]):
    for j in range(np.shape(forest)[1]):
        range_h = view_score(forest[0:i,j][::-1],forest)
        range_b = view_score(forest[i+1:,j]     ,forest)
        range_g = view_score(forest[i,0:j][::-1],forest)
        range_d = view_score(forest[i,j+1:]     ,forest)
        score[i,j] = range_h*range_b*range_g*range_d

print(np.max(score))
