from pathPlanning import *
from map import *
import csv
import os


map = GRAPH("map2_unmark.csv")

astar = Algorithm(map.adj_list, map.map_matrix)

print(astar.Astar(0, 31))

