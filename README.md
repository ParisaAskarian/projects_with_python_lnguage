def AStarSearch(self,environment):
        self.FindGoalState(environment)
        self.CaculateFNode(environment)
        self.frontier[self.current_state] = self.f_nodes[self.current_state]
        
        while self.frontier and self.energy > 0:
            min_pos = min(self.frontier,key=self.frontier.get)
            state = self.CheckState(min_pos)
            if state != 'wall' and min_pos != (0,0):
                self.logs['steps'] += 1
                self.logs['energy_used'] += 1
                self.current_state = min_pos
                self.exponend[self.current_state] = self.frontier[self.current_state]        

            if state == 'resource':
                if self.energy - 2 >= 0:
                    #for pickup item
                    self.energy -= 2
                    self.items += 1
                    self.logs['energy_used'] += 2
                    self.logs['rsource_collected'] += 1

            if state == 'hazard':
                self.logs['hzard_hits'] += 1
                if self.energy - 3 >= 0:
                    #for runaway from hazard
                    self.energy -= 3
                    self.logs['energy_used'] += 3
                else :
                    self.energy = 0
                    break
                
            if state == 'empty':
                self.energy -= 1        
            if state != 'wall':
                self.memory['visited'].append(self.current_state)
                if state == 'goal':
                    break   
                #child = {position : f(n)}
                child = self.ChildStates(environment)
                for  pos, node in child.items():
                    self.frontier[pos] = node
                self.frontier.pop(self.current_state)    

            elif state == 'wall':
                self.frontier.pop(min_pos) 
            elif state == 'goal':
                self.memory['visited'].append(self.current_state)
                self.energy -= 1    
                break 
        print(self.exponend)    
        return    
