import numpy as np
import copy

fic = open('input2.txt')
lines = fic.readlines()
fic.close()

# -------------------------- FUNCTIONS -------------------------
def flatten(list):
    return [elem  for sublist in list for elem in sublist]

# -------------------------- CLASS -----------------------------
class Valve:
    valves = []
    valves_dict = {}
    valves_connect = {}
    names_connected = {}
    not_zero = 0
    def __init__(self,name,flowrate,names):
        self.name = name
        self.flow = flowrate
        if self.flow>0:
            Valve.not_zero += 1
        self.names = names
        Valve.valves.append(self)
        Valve.valves_dict[name]=self
    def assemble():
        for valve in Valve.valves:
            Valve.valves_connect[valve] = [Valve.valves_dict[valve_connected] for valve_connected in valve.names]
            Valve.names_connected[valve.name] = [valve_connected for valve_connected in valve.names]

class State:
    def __init__(self,states):
        self.states = states
        self.pressures = {key:0 for key in self.states.keys()}
        self.opened = []
        self.final_state = 0
        self.curser=0
        self.current_valve=Valve.valves_dict['AA']
        self.path=''
    
    def compute_pressure(self):
        self.pressures = {key:sum(Valve.valves_dict[key].flow*self.states[key]) for key in self.states.keys()}
        self.final_state = sum(self.pressures.values())
    
    def open_current_valve(self,useless_buffer):
        if(self.states[self.current_valve.name][self.curser]==1) : raise Exception('Already open')
        self.states[self.current_valve.name][self.curser+1:]=1
        self.curser+=1
        self.opened.append(self.current_valve.name)
    
    def move_to_valve(self,valve):
        if(not valve in Valve.valves_connect[self.current_valve]) : raise Exception('Teleportation not allowed')
        self.current_valve=valve
        self.curser+=1

    def construct_tree(self,iterations):
        if(iterations==1):
            return self.interisting_moves()
        else:
            return flatten([state.construct_tree(iterations=iterations-1) for state in self.interisting_moves()])
    
    def how_to_move_to_valve(self,target):
        visited = []
        next_valve = self.current_valve
        path = []
        queue = [(valve,path+[valve.name]) for valve in Valve.valves_connect[next_valve]]
        while (len(queue)!=0 and next_valve!=target):
            next_valve,path = queue.pop(0)
            queue += [(valve,path+[valve.name]) for valve in Valve.valves_connect[next_valve] if valve not in visited]
            visited.append(next_valve)
        return path
    
    def interisting_moves(self):
        closed_valves = [valve for valve in Valve.valves if (valve.name not in self.opened and valve.flow>0)]
        future_states = []
        for valve in closed_valves:
            path=self.how_to_move_to_valve(valve)
            fut_state = copy.copy(self)
            fut_state.states = copy.deepcopy(self.states)
            fut_state.opened = copy.deepcopy(self.opened)
            if len(path)+fut_state.curser<=29:
                for name in path:
                    fut_state.move_to_valve(Valve.valves_dict[name])
                    fut_state.path += 'Move to valve '+name+' || '
                fut_state.open_current_valve(0)
                fut_state.path += 'Open valve '+fut_state.current_valve.name+' || '
                fut_state.compute_pressure()
                future_states.append(fut_state)
        if(len(future_states)==0): return [self]
        return future_states

    

# -------------------------- PARSER ----------------------------
for line in lines:
    first_part,second_part = line.strip().split(';')
    ffpart,fr = first_part.split('=')
    name = ffpart.split(' ')[1]
    names = [elem[-2:] for elem in second_part.split(',')]
    Valve(name,int(fr),names)

Valve.assemble()

# ------------------------- ALGORITHMIQUE ----------------------

states = {valve.name:np.array([0]*30) for valve in Valve.valves}
s = State(states)

best_candidate = None
best_score = -1

print(Valve.not_zero)

all_states = {state:state.final_state for state in s.construct_tree(iterations=5)}

sorted_states = sorted(all_states.items(),key= lambda item:item[1],reverse=True)

best_state = sorted_states[0][0]

print(best_state.path,best_state.final_state)