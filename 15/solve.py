fic = open('input.txt','r')
lines = fic.readlines()
fic.close()
fic_out = open('solve.out','w')

import numpy as np

class Beacon:
    beacons = []
    xs = []
    ys = []
    xys = []

    def __init__(self,x,y):
        self.x = x
        self.y = y
        if((x,y) not in Beacon.xys):
            Beacon.xys.append((x,y))
            Beacon.beacons.append(self)

class Sensor :
    sensors = []
    def __init__(self,x,y,beacon,distance):
        self.x = x
        self.y = y
        self.beaconx = beacon.x
        self.beacony = beacon.y
        self.distance = distance

        Sensor.sensors.append(self)

class Interval:
    intervals = []
    def __init__(self,xmi,xma):
        self.xmi = xmi
        self.xma = xma
    def fusionnable(self,interv):
        return self.xma>=interv.xmi or interv.xma>=self.xmi
    def fusion(self,interv):
        if self.fusionnable(interv):
            return min(self.xmi,interv.xmi),max(self.xma,interv.xma)
    def getgud(self):
        hasbeenfusioned = False
        for i in Interval.intervals:
            if self.fusionnable(i):
                mi,ma = i.fusion(self)
                i.xmi = mi
                i.xma = ma
                hasbeenfusioned = True
                break        
        if(not hasbeenfusioned) : Interval.intervals.append(self)


for line in lines:
    a = line.strip().split(':')
    a = [elem.split('=') for elem in a]
    x1 = int(a[0][1][:-3])
    y1 = int(a[0][2])
    x2 = int(a[1][1][:-3])
    y2 = int(a[1][2])

    beac = Beacon(x2,y2)
    sens = Sensor(x1,y1,beac,abs(x2-x1)+abs(y2-y1))

yc = 2000000

for i,s in enumerate(Sensor.sensors):
    diffy = abs(s.y-yc)
    if diffy>s.distance : 
        pass
    else:
        interv = Interval(s.x-s.distance+diffy,s.x+s.distance-diffy)
        interv.getgud()

number_beacs = 0
for beac in Beacon.beacons:
    if beac.y == yc :
        number_beacs += 1

for i in Interval.intervals:
    print('Interval final')
    print(i.xmi,i.xma,(i.xma-i.xmi+1),number_beacs,(i.xma-i.xmi+1)-number_beacs)
