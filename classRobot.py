import math
import numpy as np
import pygame
# Khởi tạo Pygame
pygame.init()

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Model")

class Robot:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.left_wheel_speed = 1
        self.right_wheel_speed = 3
        self.l = 60
        self.angle = 0
        self.ICC_radius = 0
        self.ICC_w = 0
        self.ICC_center = np.array([0,0])
        self.angle = math.pi/2
        self.ICC_radius = self.l / 2 * (self.left_wheel_speed + self.right_wheel_speed) / (self.right_wheel_speed - self.left_wheel_speed)
        self.ICC_w = (self.left_wheel_speed - self.right_wheel_speed)/ self.l
        self.ICC_center = np.array([self.x - self.ICC_radius * math.sin(self.angle),self.y + self.ICC_radius * math.cos(self.angle)])

        self.timestep = 0.5

    def updatePose(self):
        self.x = math.cos(self.ICC_w*self.timestep) * (self.x - self.ICC_center[0]) - math.sin(self.ICC_w*self.timestep) * (self.y - self.ICC_center[1]) + self.ICC_center[0]
        self.y = math.sin(self.ICC_w*self.timestep) * (self.x - self.ICC_center[0]) + math.cos(self.ICC_w*self.timestep) * (self.y - self.ICC_center[1]) + self.ICC_center[1]
        self.angle += self.ICC_w*self.timestep
        # self.ICC_center = np.array([self.x - self.ICC_radius * math.sin(self.angle),self.y + self.ICC_radius * math.cos(self.angle)])

    
    # def movetoGoal(self,goal):
    #     theta = np.arctan2(goal[1] - self.y, goal[0] - self.x)
    #     angular_vel = theta - self.angle
    #     linear_vel = np.linalg.norm([goal[0] - self.x, goal[1] - self.y])
    #     self.left_wheel_speed = 1/2 * linear_vel + self.l/2 * angular_vel
    #     self.right_wheel_speed = 1/2 * linear_vel - self.l/2 * angular_vel
    #     self.angle = math.pi/2
    #     self.ICC_radius = self.l / 2 * (self.left_wheel_speed + self.right_wheel_speed) / (self.right_wheel_speed - self.left_wheel_speed)
    #     self.ICC_w = (self.left_wheel_speed - self.right_wheel_speed)/ self.l
    #     self.ICC_center = np.array([self.x - self.ICC_radius * math.sin(self.angle),self.y + self.ICC_radius * math.cos(self.angle)])
    #     self.updatePose()
        

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), 30)
        end_x = self.x + 30 * math.cos(self.angle)
        end_y = self.y + 30 * math.sin(self.angle)
        pygame.draw.line(screen, GREEN, (int(self.x), int(self.y)), (int(end_x), int(end_y)), 5)
        pygame.draw.line(screen, BLUE, (int(self.x), int(self.y)), (int(self.ICC_center[0]), int(self.ICC_center[1])), 5)

robot = Robot(200,200)


# robot = Robot(WIDTH // 2, HEIGHT // 2)


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(WHITE)

    # robot.movetoGoal([400,400])
    robot.updatePose()
    robot.draw()



    pygame.display.flip()
    clock.tick(120)

pygame.quit()