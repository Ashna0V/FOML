# defining the goals, actions,reward and the punishments
import sys

sys.setrecursionlimit(10000)
actions = [(0,1),(0,-1),(1,0),(-1,0)] #right #left #down #up
start = [(3,0)]
state = [(0,0)]
experience = [] #to store the actions that gave negative reward or impossible move
rewards = [(2,2),(0,3)]
punishments = [(1,1),(1,2),(3,1),(3,2),(2,3)]
end = [(0,3)]
path =[]

# Start the algorithm

def start_algorithm(path,start,end,state,experience,actions,punishments,loop):
    state[0] = start[0]
    path.append(start[0])
    def continue_algorithm(path,start,end,state,experience,actions,punishments,loop):
        flag = 0
        stuck = 1
        current_state = state[0]
        for i in actions:
            for j in experience:
                if current_state in j and j[current_state] == i:
                    flag = 1
                    break
            if( flag ==1 ):
                flag = 0 
                continue
            if state[0][0] + i[0] > 3 or state[0][0] + i[0] < 0 or state[0][1] + i[1] > 4 or state[0][1] + i[1] < 0: 
                experience.append({state[0] : i})
                continue
            if (state[0][0]+i[0],state[0][1]+i[1]) in path:
                continue
            else:
                state[0] = state[0][0]+i[0],state[0][1]+i[1]
                path.append(state[0])
            if state[0] in punishments:
                experience.append({current_state : i})
                path.clear()
                return start_algorithm(path,start,end,state,experience,actions,punishments,loop)
            if state[0] == end[0]:
                return path,experience
            stuck = 0
            break
        if(stuck == 1):
            stuck = 1
            experience.append({path[-2] : (current_state[0] - path[-2][0] , current_state[1] - path[-2][1])})
            path.clear()
            return start_algorithm(path,start,end,state,experience,actions,punishments,loop)
        loop = loop - 1
        return continue_algorithm(path,start,end,state,experience,actions,punishments,loop) 
    return continue_algorithm(path,start,end,state,experience,actions,punishments,loop)
  
 
#calling the function
print(start_algorithm(path,start,end,state,experience,actions,punishments,30)[0])
