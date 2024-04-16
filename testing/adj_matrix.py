from pathPlanning import *

def create_adj_list(matrix):
    rows, cols = len(matrix), len(matrix[0])
    adj_list = {}

    def index(row, col):
        return row * cols + col

    for row in range(rows):
        for col in range(cols):
            directions = matrix[row][col]
            current_index = index(row, col)
            adj_list[current_index] = []

            if directions == 0:
                if row > 0 and matrix[row - 1][col] == 0:
                    adj_list[current_index].append(index(row - 1, col))
                if row < rows - 1 and matrix[row + 1][col] == 0:
                    adj_list[current_index].append(index(row + 1, col))
                if col > 0 and matrix[row][col - 1] == 0:
                    adj_list[current_index].append(index(row, col - 1))
                if col < cols - 1 and matrix[row][col + 1] == 0:
                    adj_list[current_index].append(index(row, col + 1))

    return adj_list

# Example usage
matrix = [[0, 0, 0, 1, 0], [0, 1, 0, 0, 0]]
adj_list = create_adj_list(matrix)
astar = Algorithm(adj_list, matrix)
print(astar.Astar(0, 8))
print(adj_list)


