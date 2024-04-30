import numpy as np
import pygame
from map import *

class ROBOT:
    def __init__(self,initial_pos):    
        self.target_pos = np.array([0,0])
        self.current_pos = initial_pos
        self.velocity = np.zeros(2).astype(int)
        self.color = (200, 0, 0)
        self.trace = []
        # self.map = map
    
    def updatePose(self):
        if np.linalg.norm(self.current_pos - self.target_pos) < 0.01:
            self.velocity = np.zeros(2)
        else:
            self.current_pos = self.current_pos + self.velocity
            self.trace.append(self.current_pos)

    def movetoGoal(self,goal, pre_goal):
        if (goal - pre_goal) == 1:
            self.velocity = np.array([1,0])
        elif (goal - pre_goal) == -1:
            self.velocity = np.array([-1,0])
        elif (goal - pre_goal) == 30:
            self.velocity = np.array([0,1])
        elif (goal - pre_goal) == -30:
            self.velocity = np.array([0,-1])
        
        

    