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
           [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
           [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1], 
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0], 
           [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1], 
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]]
print(len(rewards), len(rewards[0]))
rewards = np.array(rewards)
print(rewards.size(), len(rewards))
