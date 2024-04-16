import csv
import os

class DATA:
    def __init__(self, filename):
        self.filename = filename
        self.map_matrix = self.read_csv()
        self.adj_list = self.create_weighted_adj_list()
        