import csv
import os

class GRAPH:
    def __init__(self, filename):
        self.filename = filename
        self.map_matrix = self.read_csv(filename)
        self.adj_list = self.create_weighted_adj_list()
        
        
    def create_weighted_adj_list(self):
        rows, cols = len(self.map_matrix), len(self.map_matrix[0])
        adj_list = {}

        def index(row, col):
            return row * cols + col

        for row in range(rows):
            for col in range(cols):
                weight = self.map_matrix[row][col]
                current_index = index(row, col)
                adj_list[current_index] = []

                if weight == 0:
                    if row > 0 and self.map_matrix[row - 1][col] == 0:
                        adj_list[current_index].append((index(row - 1, col), 1))  # Weight is 1 for adjacent nodes
                    if row < rows - 1 and self.map_matrix[row + 1][col] == 0:
                        adj_list[current_index].append((index(row + 1, col), 1))
                    if col > 0 and self.map_matrix[row][col - 1] == 0:
                        adj_list[current_index].append((index(row, col - 1), 1))
                    if col < cols - 1 and self.map_matrix[row][col + 1] == 0:
                        adj_list[current_index].append((index(row, col + 1), 1))
        
        return adj_list
    
    def read_csv(self,filename):
        map_data = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=",")
            for row in data:
                result_list = [int(item) if item != '' else 0 for item in row]
                # print(result_list)
                map_data.append(list(result_list))
        # print(map_data)
        return map_data
    