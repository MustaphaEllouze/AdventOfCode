import numpy as np

fic = open('input.txt','r')
lines = [line.strip() for line in fic.readlines()]
fic.close()

alpha = 'abcdefghijklmnopqrstuvwxyz'
dican = {a:(i+1) for i,a in enumerate(list(alpha))}
dican['S']=0
dican['E']=27

map = np.array([[dican[c] for c in list(line)] for line in lines])

path = np.array([[-1] * np.shape(map)[1]]* np.shape(map)[0])

arr = np.where(map==1)
dep = np.where(map==27)

queue = [(dep,27,0,'.',dep)]
current = dep
visited = []
iter = 0

while(len(queue)!=0 and map[tuple(current)] != 1):
    current,hei,depth,sens,last = queue.pop(0)
    if not (list(current) in visited):
        iter += 1
        visited.append(list(current))
        path[current]=depth
        
        to_add = tuple(np.array([current[0],current[1]-1]))
        if(current[1]>0 and (-int(map[to_add])+hei)<=1):
            queue.append((to_add,int(map[to_add]),depth+1,'<',current))
        
        to_add = tuple(np.array([current[0],current[1]+1]))
        if(current[1]<np.shape(map)[1]-1 and (-int(map[to_add])+hei)<=1):
            queue.append((to_add,int(map[to_add]),depth+1,'>',current))

        to_add = tuple(np.array([current[0]-1,current[1]]))
        if(current[0]>0 and (-int(map[to_add])+hei)<=1):
            queue.append((to_add,int(map[to_add]),depth+1,'^',current))

        to_add = tuple(np.array([current[0]+1,current[1]]))
        if(current[0]<np.shape(map)[0]-1 and (-int(map[to_add])+hei)<=1):
            queue.append((to_add,int(map[to_add]),depth+1,'v',current))

print('sol = ' + str(np.max(path[tuple(arr)])))
