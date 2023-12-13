import numpy as np

alpha = 0.8
gamma = 0.75

actions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
location_to_state = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11}
state_to_location = {s:l for s, l in location_to_state.items()}
rewards = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
           [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
           [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
           [0, 0, 1, 0, 0, 0, 1000, 1, 0, 0, 0, 0], 
           [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1], 
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0], 
           [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], 
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]]
rewards = np.array(rewards)

def get_route(starting, ending):
           new_rewards = np.copy(rewards)
           end_pos = location_to_state[ending]
           new_rewards[end_pos, end_pos] = 1000
           Q = np.zeros([12, 12])
           for _ in range(1000):
                      state = np.random.randint(0, 12)
                      playable = []
                      print(state)
                      for ind in range(12):
                                 if Q[state, ind] != 0:
                                            playable.append(ind)
                      # print(playable)
                      next_state = np.random.choice(playable)
                      TD = rewards[state, next_state] + gamma * Q[next_state, np.argmax(Q[next_state, ])] - Q[state, next_state]
                      Q[state, next_state] = Q[state, next_state] + alpha * TD
           route = [starting]
           next_pos = starting
           while next_pos != ending:
                      start_state = location_to_state[starting]
                      next_state = np.argmax(Q[start_state, ])
                      next_pos = state_to_location(Q[next_state, ])
                      route.append(next_pos)
                      starting = next_pos
           return route
res = get_route('A', 'B') + get_route('B', 'G')[1:]
print(res)
print(res == ['A', 'B', 'C', 'G'])
