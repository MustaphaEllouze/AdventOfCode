fic = open('input.txt','r')
lines = fic.readlines()
fic.close()

class Monkey():

    monkeys = []

    def __init__(self,number,items,operation,test,true_do,false_do):
        self.number = int(number)
        self.items = [int(item) for item in items]
        self.operation = operation
        self.test = int(test)
        self.true_do = int(true_do)
        self.false_do = int(false_do)
        self.inspects = 0

        Monkey.monkeys.append(self)
    
    def treat_items (self):
        while len(self.items)!=0:
            self.inspects += 1
            item = self.items.pop(0)
            #print('    Monkey inspects an item with a worry level of '+str(item))
            secondterme = self.operation[-1]
            if(not secondterme.isdigit()):
                secondterme = item
            else:
                secondterme = int(secondterme)    
            if(self.operation[0]=='+'):
                item = item+secondterme
                #print('        Worry level increases by '+str(secondterme)+' to '+str(item))
            if(self.operation[0]=='*'):
                item = item*secondterme
                #print('        Worry level is multiplied by '+str(secondterme)+' to '+str(item))
            item = item // 3
            #print('        Monkey gets bored with item. Worry level is divided by 3 to ' + str(item))
            if(item%self.test==0):
                Monkey.monkeys[self.true_do].items.append(item)
                #print('        Current worry level is divisible by '+str(self.test))
                #print('        Item with worry level '+str(item)+'is thrown to monkey '+str(self.true_do))
            else:
                Monkey.monkeys[self.false_do].items.append(item)
                #print('        Current worry level is not divisible by '+str(self.test))
                #print('        Item with worry level '+str(item)+' is thrown to monkey '+str(self.false_do))


# i%7=0 : Monkey 0:
# i%7=1 :   Starting items: 79, 98
# i%7=2 :   Operation: new = old * 19
# i%7=3 :   Test: divisible by 23
# i%7=4 :     If true: throw to monkey 2
# i%7=5 :     If false: throw to monkey 3
# i%7=6 : 
# i%7=0 : Monkey 1:

number = -1
items = []
operation = ['',0]
test = -1
true_do = -1
false_do = -1

for i,line in enumerate(lines):
    
    a = line.split()
    if(i%7==0):
        number = a[1][:-1]
    elif(i%7==1):
        items = [elem[:-1] for elem in a[2:-1]]+[a[-1]]
    elif(i%7==2):
        operation = [a[-2],a[-1]]
    elif(i%7==3):
        test = a[-1]
    elif(i%7==4):
        true_do = a[-1]
    elif(i%7==5):
        false_do = a[-1]
        Monkey(number,items,operation,test,true_do,false_do)

for i in range(20):
    for monkey in Monkey.monkeys :
        #print('Monkey '+str(monkey.number)+':')
        monkey.treat_items()
    print(str(i)+'\\10000')

print([m.inspects for m in Monkey.monkeys])

    