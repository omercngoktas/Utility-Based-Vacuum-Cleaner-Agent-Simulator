class Robot:
    def __init__(self, name, initial_room, rooms, robot_type):
        self.name = name
        self.current_room = initial_room
        self.rooms = rooms
        self.robot_type = robot_type
        
        self.total_score = 0
        self.direction = "right"
        self.logout = ""
        self.room_visits = {"A": 0, "B": 0, "C": 0}
        self.state_count = {"A": 0, "B": 0, "C": 0}
        self.state_list = {"A": [], "B": [], "C": []}
        
    # decreases point by 0.5 for agent B
    def decrease_point(self, point=0.5):
        if self.robot_type == "B": self.total_score -= point
    
    # increases point by 1 for all agents
    def increase_point(self, point=1):
        if self.rooms["A"].is_room_dirty() == False:
            print("A arttı")
            self.total_score += point
            
        if self.rooms["B"].is_room_dirty() == False:
            print("B arttı")
            self.total_score += point
            
            
        if self.rooms["C"].is_room_dirty() == False:
            print("C arttı")
            self.total_score += point
    
    # increases visit point for current room
    def increase_room_visits(self):
        self.room_visits[self.current_room.name] += 1
        
    # cleans current room, increases point, then rooms get dirty accordingly probability
    def clean_room(self):
        self.logout_current_room_with_state()
        self.current_room.clean()
        self.logout += "suck\n"
        self.increase_point()
        self.logout_current_room_with_state()
        self.make_rooms_dirty()
        self.logout_total_score()
        
    def logout_total_score(self):
        self.logout += f"{self.total_score}\n\n"
        
    # moves the agent to left
    def move_left(self):
        if self.current_room != self.rooms["A"]:
            self.logout_current_room_with_state()
            self.logout += "Left\n"
            if self.current_room == self.rooms["B"]:
                self.current_room = self.rooms["A"]
                
            elif self.current_room == self.rooms["C"]:
                self.current_room = self.rooms["B"]

            self.logout_current_room_with_state()
            self.make_rooms_dirty()
            self.decrease_point()
            self.logout_total_score()
            return True
        
        elif self.current_room == self.rooms["A"]:
            return False
    
    # moves the agent to right
    def move_right(self):
        if self.current_room != self.rooms["C"]:
            self.logout_current_room_with_state()
            self.logout += "Right\n"
            if self.current_room == self.rooms["B"]:
                self.current_room = self.rooms["C"]
            
            elif self.current_room == self.rooms["A"]:
                self.current_room = self.rooms["B"]
                
            self.logout_current_room_with_state()
            self.make_rooms_dirty()
            self.decrease_point()
            self.logout_total_score()
            return True
            
        elif self.current_room == self.rooms["C"]:
            return False
        
    # checks if the agent can move right
    def can_move_right(self):
        if self.current_room.name != "C":
            return True
        return False
    
    # checks if the agent can move left
    def can_move_left(self):
        if self.current_room.name != "A":
            return True
        return False
            
    # no operation, the agent will wait
    def no_op(self):
        self.logout_current_room_with_state()
        self.make_rooms_dirty()
        self.logout += "no-op\n"
        self.logout_current_room_with_state()
        self.increase_room_visits()
        self.increase_point()
        self.logout_total_score()

    # according to probabilities, makes rooms dirty
    def make_rooms_dirty(self):
        if self.rooms["A"].is_dirty == False:
            self.rooms["A"].make_dirty()

        if self.rooms["B"].is_dirty == False:
            self.rooms["B"].make_dirty()

        if self.rooms["C"].is_dirty == False:
            self.rooms["C"].make_dirty()
    
    # moves robot according to current direction
    def move_robot(self, is_increase_point=True):
        if is_increase_point == True:
            self.increase_point()
            
        # Check if direction is "right"
        if self.direction == "right":
            # Can move to right
            if self.can_move_right():
                
                self.move_right()
                self.increase_room_visits()
                
                return True
            # Cannot move right, should move left
            else:
                self.direction = "left"
                return False
        
        # Direction is "left"
        else:
            # Can move to left
            if self.can_move_left():
                self.move_left()
                return True
                
            # Cannot move to left, should move right
            else:
                self.direction = "right"
                return False
        
    def logout_current_room_with_state(self):
        self.logout += f"{self.current_room.name}, {self.rooms["A"].return_state()}, {self.rooms["B"].return_state()}, {self.rooms["C"].return_state()}\n"

    # training robot to learn dirty probabilities
    def train_robot(self, test_size=0.33, time_steps=1000):
        test_size = int(time_steps * test_size)
        for i in range(test_size):
            self.logout += f"Step {i + 1}\n"
            self.state_count[self.current_room.name] += 1
            self.state_list[self.current_room.name].append(self.rooms[self.current_room.name].return_state())
            # Room is dirty
            if self.current_room.is_room_dirty():
                self.clean_room()
                continue
            # Room is clean
            elif not self.current_room.is_room_dirty():
                state = self.move_robot()
                if state == False:
                    self.move_robot(is_increase_point = False)
                    continue
        # printing the each time state with room states
        for room in self.state_count.keys():
            filename = f"Prob_{room}-Agent_{self.name}.txt"
            with open(filename, 'w') as file:
                file.write("count,room_state\n")
                for count, index in enumerate(self.state_list[room], start=1):
                    file.write(f"{count},{index}\n")

    def print_line(self):
        self.logout += f"{'-'*50}\n"
    
    def decide_next_action(self, dirt_probabilities, last_cleaned):
        if self.current_room.is_room_dirty():
            return "clean"
        
        next_room = None
        highest_score = -1
        for room, probability in dirt_probabilities.items():
            if room != self.current_room.name:
                score = probability - last_cleaned[room] * 0.1
                if score > highest_score:
                    highest_score = score
                    next_room = room
        
        if next_room is None:
            return 'no_op'
        if next_room < self.current_room.name:
            return 'left'
        elif next_room > self.current_room.name:
            return 'right'
    
    def simulate_cleaning(self, dirt_probabilities, time_steps, file_name, last_steps=1000):
        last_cleaned = {"A": 1, "B": 1, "C": 1}
        last_cleaned[self.current_room.name] = 0
        
        for step in range(time_steps):
            self.logout += f"Step {step + (last_steps-time_steps) + 1}\n"
            next_step = self.decide_next_action(dirt_probabilities=dirt_probabilities, last_cleaned=last_cleaned)
            
            if next_step == "clean":
                self.clean_room()
                last_cleaned[self.current_room.name] = 0
            else:
                if next_step == "no_op":
                    self.no_op()
                    for room in last_cleaned:
                        last_cleaned[room] += 1
                    
                elif next_step in ["right", "left"]:
                    self.direction = next_step
                    self.move_robot()
                    for room in last_cleaned:
                        last_cleaned[room] += 1
                    last_cleaned[self.current_room.name] = 0
        # save result to file
        with open(file_name, "w") as file:
            file.write(self.logout)
            
    def __str__(self):
        return f""