import pandas as pd
import random
import sys
from room import Room
from robot import Robot

def calculate_dirt_probabilities(file_paths):
    probabilities = {}
    for room, file_path in file_paths.items():
        data = pd.read_csv(file_path)
        dirty_states_count = (data['room_state'] == 'D').sum()
        probability = dirty_states_count / len(data)
        probabilities[room] = probability
    return probabilities

def normalize_probabilities(dirt_probabilities):
    max_prob = max(dirt_probabilities.values())
    if max_prob > 0:
        for room in dirt_probabilities:
            dirt_probabilities[room] /= max_prob
    else:
        # Eğer tüm olasılıklar 0 ise, tüm odalara eşit olasılık atanır
        for room in dirt_probabilities:
            dirt_probabilities[room] = 1.0
    
    return dirt_probabilities

def main():
    if len(sys.argv) != 6:
        print("Usage: python main.py Pa Pb Pc output_a output_b")
        return
    
    try:
        Pa = float(sys.argv[1])
        Pb = float(sys.argv[2])
        Pc = float(sys.argv[3])
        
    except Exception as e:
        print(e)
    
    rooms = {
        "A": Room(name="A", probability=Pa, is_dirty=True),
        "B": Room(name="B", probability=Pb, is_dirty=True),
        "C": Room(name="C", probability=Pc, is_dirty=True)
    }
    
    file_paths_agent_A = {
        "A": "./Prob_A-Agent_A.txt",
        "B": "./Prob_B-Agent_A.txt",
        "C": "./Prob_C-Agent_A.txt"
    }
    
    file_paths_agent_B = {
        "A": "./Prob_A-Agent_B.txt",
        "B": "./Prob_B-Agent_B.txt",
        "C": "./Prob_C-Agent_B.txt"
    }
    
    agent_A = Robot(name="A", initial_room=rooms["B"], rooms=rooms, robot_type="A")
    agent_B = Robot(name="B", initial_room=rooms["B"], rooms=rooms, robot_type="B")
    
    time_steps = 1000
    test_size = 0.33
    remain_steps = int(time_steps - (time_steps * test_size))
    
    agent_A.train_robot(test_size=test_size, time_steps=time_steps)
    dirt_probabilities_agent_A = calculate_dirt_probabilities(file_paths_agent_A)
    agent_A.simulate_cleaning(dirt_probabilities=dirt_probabilities_agent_A, time_steps=remain_steps, file_name=sys.argv[4])


    agent_B.train_robot(test_size=test_size, time_steps=time_steps)
    dirt_probabilities_agent_B = calculate_dirt_probabilities(file_paths_agent_B)
    agent_B.simulate_cleaning(dirt_probabilities=dirt_probabilities_agent_B, time_steps=remain_steps, file_name=sys.argv[5])
    
if __name__ == "__main__":
    main()
    
    
    