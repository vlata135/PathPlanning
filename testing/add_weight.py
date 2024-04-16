from pathPlanning import Algorithm
def create_weighted_adj_list(matrix):
    rows, cols = len(matrix), len(matrix[0])
    adj_list = {}

    def index(row, col):
        return row * cols + col

    for row in range(rows):
        for col in range(cols):
            weight = matrix[row][col]
            current_index = index(row, col)
            adj_list[current_index] = []

            if weight == 0:
                if row > 0 and matrix[row - 1][col] == 0:
                    adj_list[current_index].append((index(row - 1, col), 1))  # Weight is 1 for adjacent nodes
                if row < rows - 1 and matrix[row + 1][col] == 0:
                    adj_list[current_index].append((index(row + 1, col), 1))
                if col > 0 and matrix[row][col - 1] == 0:
                    adj_list[current_index].append((index(row, col - 1), 1))
                if col < cols - 1 and matrix[row][col + 1] == 0:
                    adj_list[current_index].append((index(row, col + 1), 1))

    return adj_list

# Example usage
matrix = [[0, 0, 0, 1, 0], [0, 1, 0, 0, 0]]
weighted_adj_list = create_weighted_adj_list(matrix)
astar = Algorithm(weighted_adj_list, matrix)

print(weighted_adj_list)
