import pygame
import numpy as np
from robot import *
from map import *
import math
import random
from pathPlanning import *
import time

class DRAW:
    def __init__(self,map_matrix):
        self.width = 600
        self.height = 600
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Path Planning")
        # self.num_robots = num_robots
        self.map_matrix = map_matrix
        self.centers = self.getPosition()
        

    def get_rect(self,x, y):
        return x * 20, y * 20, 20, 20
    
    def getPosition(self):
        centers = []
        for i in range(len(self.map_matrix)):
            for j in range(len(self.map_matrix[0])):
                rect1 = pygame.Rect(self.get_rect(j,i))
                centers.append(rect1.center)  
        # center = matrix_to_array(center)
        # print(center[1])

        return centers


    def draw_robot(self,robot):
        pygame.draw.circle(self.screen, robot.color, (int(robot.current_pos[0]), int(robot.current_pos[1])), 10)
        # for i in range(len(robot.trace)):
        #     pygame.draw.circle(self.screen, (255,215,0), (int(robot.trace[i][0]), int(robot.trace[i][1])), 2)
        #     if i > 0:
        #         pygame.draw.line(self.screen, (255,215,0), (int(robot.trace[i][0]), int(robot.trace[i][1])), (int(robot.trace[i-1][0]), int(robot.trace[i-1][1])), 2)

    def draw_map(self):
        rows, cols = len(self.map_matrix), len(self.map_matrix[0])
        for row in range(rows):
            for col in range(cols):
                if self.map_matrix[row][col] == 1:
                    pygame.draw.rect(self.screen, (0,0,0), (col * 20, row * 20, 20, 20))
                else:
                    pygame.draw.rect(self.screen, (255,255,255), (col * 20, row * 20, 20, 20))

    def drawMove(self,path):
        for point in path:
            pygame.draw.circle(self.screen, pygame.Color('blue'), self.centers[point], 4)
        for point in path:
            pygame.draw.circle(self.screen, pygame.Color('blue'), self.centers[point], 4)

    def plot(self):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        
        #469
        init_point = 31
        target_point = 867
        init_pos = self.centers[init_point]
        target_pos = self.centers[target_point]
        
        robot = ROBOT(init_pos)
        # self.map_matrix = map.map_matrix
        
        path = astar.Astar(init_point, target_point)
        print(path)

        
        # Create a map
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # self.screen.fill(WHITE)
            # self.draw_map()
            if path != []:
                pre_goal = path[0] - 1
            while path != []:
                self.screen.fill(WHITE)
                self.draw_map()
                self.drawMove(path)
                
                robot.movetoGoal(path[0], pre_goal)
                print(np.linalg.norm(robot.current_pos - np.array(self.centers[path[0]])))
                if np.linalg.norm(robot.current_pos - np.array(self.centers[path[0]])) < 1.5 and path != []:
                    pre_goal = path[0]
                    path.pop(0)
                    # print(path[0], pre_goal)
                robot.updatePose()
                self.draw_robot(robot)
                if path == []:
                    break

            
                pygame.display.flip()
                self.clock.tick(60)
            
        pygame.quit()

    

if __name__ == "__main__":
    
    map = GRAPH("map2_unmark.csv")

    astar = Algorithm(map.adj_list, map.map_matrix)
    draw = DRAW(map.map_matrix)
    
    # print(draw.map_matrix)

    draw.plot()
    

    