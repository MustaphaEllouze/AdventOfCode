import numpy as np
import copy

fic = open('input.txt')
lines = fic.readlines()
fic.close()

# -------------------------- CLASS -----------------------------
class Valve:
    valves = []
    valves_dict = {}
    valves_connect = {}
    names_connected = {}
    def __init__(self,name,flowrate,names):
        self.name = name
        self.flow = flowrate
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
        self.final_state = 0
        self.curser=0
        self.current_valve=Valve.valves_dict['AA']
        self.path=''
    
    def compute_pressure(self):
        self.pressures = {key:sum(Valve.valves_dict[key].flow*self.states[key]) for key in self.states.keys()}
        self.final_state = sum(self.pressures.values())
    
    def possible_moves(self):
        return Valve.valves_connect[self.current_valve]
    
    def can_open_valve(self):
        return self.states[self.current_valve.name][self.curser]==0
    
    def open_current_valve(self,useless_buffer):
        if(self.states[self.current_valve.name][self.curser]==1) : raise Exception('Already open')
        self.states[self.current_valve.name][self.curser+1:]=1
        self.curser+=1
    
    def move_to_valve(self,valve):
        if(not valve in Valve.valves_connect[self.current_valve]) : raise Exception('Teleportation not allowed')
        self.current_valve=valve
        self.curser+=1
    
    def possible_actions(self):
        part_1 = [('PM',valve) for valve in self.possible_moves()]
        part_2 = [('OV',self.can_open_valve())]*self.can_open_valve()
        return part_1+part_2
    
    def future_states(self):
        possible_actions = self.possible_actions()
        future_states = []
        for action,argument in possible_actions:
            fut_state = copy.copy(self)
            fut_state.states = copy.deepcopy(self.states)
            if action=='PM':
                fut_state.path += 'Move to valve '+argument.name+' || '
                fut_state.move_to_valve(argument)
            elif(action=='OV'):
                fut_state.path += 'Open valve '+fut_state.current_valve.name+' || '
                fut_state.open_current_valve(argument)
            fut_state.compute_pressure()
            future_states.append(fut_state)
        return future_states

    def construct_tree(self,iterations):
        if(iterations==1):
            return self.future_states()
        else:
            return [state.construct_tree(iterations=iterations-1) for state in self.future_states()]
    

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

