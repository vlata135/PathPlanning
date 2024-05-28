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
        
        self.tile_size = 30
        self.length_x = 20
        self.length_y = 20
        self.width = self.tile_size * self.length_x
        self.height = self.tile_size * self.length_y
        pygame.init() 
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Path Planning")
        # self.num_robots = num_robots
        self.map_matrix = map_matrix
        self.centers = self.getPosition()
        self.pos_posible = []
    def get_rect(self,x, y):
        return x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size
    
    def getCoordinate(self, index):
        rows, cols = len(self.map_matrix), len(self.map_matrix[0])
        row = index // cols
        col = index % cols  
        return row, col
    
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
        # pygame.draw.circle(self.screen, robot.color, (int(robot.current_pos[0]), int(robot.current_pos[1])), 15)

        pygame.draw.circle(self.screen, pygame.Color("chartreuse3"), robot.current_pos, self.tile_size/3,10)
        # print(robot.current_pos)
        # for i in range(len(robot.trace)):
        #     pygame.draw.circle(self.screen, (255,215,0), (int(robot.trace[i][0]), int(robot.trace[i][1])), 2)
        #     if i > 0:
        #         pygame.draw.line(self.screen, (255,215,0), (int(robot.trace[i][0]), int(robot.trace[i][1])), (int(robot.trace[i-1][0]), int(robot.trace[i-1][1])), 2)
    def draw_target(self, target_pos): 
        pygame.draw.circle(self.screen, pygame.Color("red"), target_pos, self.tile_size/5, 10)
    def draw_map(self):
        rows, cols = len(self.map_matrix), len(self.map_matrix[0])
        for row in range(rows):
            for col in range(cols):
                if self.map_matrix[row][col] == 1:
                    pygame.draw.rect(self.screen, pygame.Color("white"), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
                    self.pos_posible.append(self.get_index(row, col))
                elif self.map_matrix[row][col] == 2:
                    pygame.draw.rect(self.screen, (255,0,0), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
                elif self.map_matrix[row][col] == 3:
                    pygame.draw.rect(self.screen, (89,100,150), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
                elif self.map_matrix[row][col] == 4:
                    pygame.draw.rect(self.screen, (79,100,150), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
                elif self.map_matrix[row][col] == 5:
                    pygame.draw.rect(self.screen, (89,140,40), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
                elif self.map_matrix[row][col] == 6:
                    pygame.draw.rect(self.screen, (13,100,150), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
                elif self.map_matrix[row][col] == 7:
                    pygame.draw.rect(self.screen, (78,40,150), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))        
                elif self.map_matrix[row][col] == 8:
                    pygame.draw.rect(self.screen, (0,30,50), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))
                elif self.map_matrix[row][col] == 9:
                    pygame.draw.rect(self.screen, pygame.Color("red"), (col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size))

    def drawMove(self,path):
        for point in path:
            pygame.draw.circle(self.screen, pygame.Color('blue'), self.centers[point], 5)
        if(len(path) > 0):
            pygame.draw.circle(self.screen, pygame.Color('darkorange'), self.centers[path[len(path) - 1]], 5)
        # for point in path:
        #     pygame.draw.circle(self.screen, pygame.Color('blue'), self.centers[point], 5)

    def get_mouse_pos(self):
        mouse_pos = pygame.mouse.get_pos()
        row = mouse_pos[1] // self.tile_size
        col = mouse_pos[0] // self.tile_size
        return self.get_index(row, col)
    def get_robot_pos(self, pos):
        mouse_pos = pos
        row = mouse_pos[1] // self.tile_size
        col = mouse_pos[0] // self.tile_size
        return self.get_index(row, col)
    
    def get_index(self, row, col):
        return row * self.length_x + col
    
    def plot(self):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        
        #469
        init_point = 13
        target_point = 17
        init_pos = self.centers[init_point]
        target_pos = self.centers[target_point]
        
        # #điểm khởi tạo
        # init_points = [301, 304, 307, 310, 313, 316]
        init_points = [157, 117, 124, 131, 98, 41]
        # #điểm đích
        target_points = [36,31,149,71,378,364]
    
            
        
        init_poses = [self.centers[point] for point in init_points]
        # target_poses = [self.centers[point] for point in target_points]
        
        robots = [ROBOT(init_pos) for init_pos in init_poses]
        paths = [astar.Astar(init_point, target_point) for init_point, target_point in zip(init_points, target_points)]
        # # print(paths)
        
        for i in range(len(robots)):
            robots[i].path = paths[i]
            robots[i].centers = self.centers
            
        
        
        robot = ROBOT(init_pos)
        # self.map_matrix = map.map_matrix
        
        path = astar.Astar(init_point, target_point)
        print(path)
        robot.path = path
        robot.centers = self.centers
        # robot.prev_goal = path[0] - 15
        
        # Create a map
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
            self.screen.fill(WHITE)
            self.draw_map()
            
            # self.drawMove(path)
            position = self.get_mouse_pos()
            print(position)
            # robot.followPath(path)
            # self.draw_robot(robot)
            
            for robot in robots:
                # targett = self.pos_posible[random.randint(0, len(self.pos_posible)-1)]
                if(robot.path == []):
                    targett = self.pos_posible[random.randint(0, len(self.pos_posible)-1)]
                    robot.path = astar.Astar(self.get_robot_pos(robot.current_pos), targett)
                
                for other_robot in robots:
                    if robot != other_robot:
                        while( np.sqrt((robot.current_pos[0] - other_robot.current_pos[0])**2 + (robot.current_pos[1] - other_robot.current_pos[1])**2) < 30):   
                            robot.velocity = [random.randint(-1,1), random.randint(-1,1)]
                            # break
                            


                robot.followPath(robot.path)
                self.draw_robot(robot)
                self.drawMove(robot.path)
            
            
            
            
            # print(position)
            # if path != []:
            #     robot.movetoGoal(path[0], init_point)
            #     robot.updatePose()
            #     self.draw_robot(robot)
                
            #     if np.linalg.norm(robot.current_pos - np.array(self.centers[path[0]])) < 1.5:
            #         init_point = path[0]
            #         path.pop(0)
            #         # print(path[0], init_point)
            #     if path == []:
            #         # break
            #         continue
            
            
            
            

            pygame.display.flip()
            self.clock.tick(30)
            
        pygame.quit()

    

    def draw_finding_path(self, queue):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.fill((255, 255, 255))

            for _, xy in queue:
                # pygame.draw.rect(self.screen, pygame.Color('darkslategray'), self.get_rect(self.getCoordinate(self.centers[queue[0][1]])), 1)
                # print("canh ke")
                # print(queue[0][1])
                col = self.getCoordinate(xy)[1]
                row = self.getCoordinate(xy)[0]
                pygame.draw.rect(self.screen, pygame.Color('darkslategray'), self.get_rect(col, row), 3)
                print("end phase")        
            pygame.display.flip()
            self.clock.tick(7)
            


if __name__ == "__main__":
    
    map = GRAPH("map.csv")

    astar = Algorithm(map.adj_list, map.map_matrix)
    draw = DRAW(map.map_matrix)
    # path = astar.Astar(0, 115)
    # print(draw.map_matrix)

    draw.plot()
    

    