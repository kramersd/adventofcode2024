import re

def get_all_diagonals_rows_columns(matrix):
    n = len(matrix)
    results = []
    total_count = 0

    # Get all diagonals from top-left to bottom-right
    for d in range(2 * n - 1):
        diagonal = []
        for i in range(max(0, d - n + 1), min(n, d + 1)):
            diagonal.append(matrix[i][d - i])
        diag_str = ''.join(diagonal)
        results.append(diag_str)
        results.append(diag_str[::-1])
    
    # Get all diagonals from top-right to bottom-left
    for d in range(2 * n - 1):
        diagonal = []
        for i in range(max(0, d - n + 1), min(n, d + 1)):
            diagonal.append(matrix[i][n - 1 - (d - i)])
        diag_str = ''.join(diagonal)
        results.append(diag_str)
        results.append(diag_str[::-1])
    
    # Get all rows:
    for row in matrix:
        row_str = ''.join(row)
        results.append(row_str)
        results.append(row_str[::-1])
    
    # Get all columns
    for col in range(n):
        column = []
        for row in matrix:
            column.append(row[col])
        col_str = ''.join(column)
        results.append(col_str)
        results.append(col_str[::-1])

    # Count occurrences of the regex in each item
    pattern = r"XMAS"
    for item in results:
        matches = re.findall(pattern, item)
        total_count += len(matches)
    
    return total_count


def part1():
    with open('puzzle4_input.txt') as f:
        lines = f.readlines()
        matrix = []
        for l in lines:
            row = [c for c in l]
            matrix.append(row)
        print(len(matrix), matrix[0])

        x = get_all_diagonals_rows_columns(matrix)
        print(x)


def find_x_shapes(grid):
    rows = len(grid)
    cols = len(grid[0])
    x_shapes = []

    for i in range(1, rows - 1):
        for j in range(1, cols - 2):
            if ((grid[i-1][j-1] == 'M' and grid[i][j] == 'A' and grid[i+1][j+1] == 'S' and
                 grid[i-1][j+1] == 'M' and grid[i+1][j-1] =='S') or 
                (grid[i-1][j-1] == 'S' and grid[i][j] == 'A' and grid[i+1][j+1] == 'M' and
                 grid[i-1][j+1] == 'S' and grid[i+1][j-1] =='M') or
                (grid[i-1][j-1] == 'M' and grid[i][j] == 'A' and grid[i+1][j+1] == 'S' and
                 grid[i-1][j+1] == 'S' and grid[i+1][j-1] =='M') or
                (grid[i-1][j-1] == 'S' and grid[i][j] == 'A' and grid[i+1][j+1] == 'M' and
                 grid[i-1][j+1] == 'M' and grid[i+1][j-1] =='S')
                ):
                x_shapes.append((i, j))
    return x_shapes

def part2():
    with open('puzzle4_input.txt') as f:
        lines = f.readlines()
        matrix = []
        for l in lines:
            row = [c for c in l]
            matrix.append(row)
        print(len(matrix), matrix[0])

        x = find_x_shapes(matrix)
        print(len(x))

part1()
part2()