# input_file_name = 'puzzle6_input.txt'
input_file_name = 'demo.txt'

def rotate_90(direction):
    if direction == 'NORTH':
        return 'EAST'
    elif direction == 'EAST':
        return 'SOUTH'
    elif direction == 'SOUTH':
        return 'WEST'
    elif direction == 'WEST':
        return 'NORTH'

def is_out_of_bounds(position, grid):
    if position[0] > len(grid) - 1 or position[0] < 0:
        return True
    elif position[1] > len(grid[0]) - 1 or position[1] < 0:
        return True
    return False

def move_piece(current_position, direction_to_move, grid):
    new_position = (current_position[0], current_position[1])
    if direction_to_move == 'NORTH':
        new_position = (current_position[0] - 1, current_position[1])
    elif direction_to_move == 'SOUTH':
        new_position = (current_position[0] + 1, current_position[1])
    elif direction_to_move == 'WEST':
        new_position = (current_position[0], current_position[1] - 1)
    elif direction_to_move == 'EAST':
        new_position = (current_position[0], current_position[1] + 1)

    if not is_out_of_bounds(new_position, grid):
        piece = grid[new_position[0]][new_position[1]]
        new_direction = ''
        if piece == '#':
            new_direction = rotate_90(direction_to_move)
            new_position = current_position
        else:
            new_direction = direction_to_move
    else:
        return (), direction_to_move, True
    
    return new_position, new_direction, False

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()

        grid = []
        for l in lines:
            l = l.strip()

            row = []
            for i in l:
                row.append(i)
            grid.append(row)

        obstacle_positions = []
        starting_point = ()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '#':
                    obstacle_positions.append((i, j))
                elif grid[i][j] == '^':
                    starting_point = (i, j)
        
        print('Starting Point', starting_point)
        # print('Obstacle Positions', obstacle_positions)
        print('?x?', len(grid), len(grid[0]))


        current_position = starting_point
        visited_points = []
        direction_to_move = 'NORTH'
        
        while (not is_out_of_bounds(current_position, grid)):
            new_position, new_direction, out_of_bounds = move_piece(current_position, direction_to_move, grid)
            if out_of_bounds:
                break
            if new_position not in visited_points:
                visited_points.append(new_position)
            current_position = new_position
            direction_to_move = new_direction
        # print('Visited Points', visited_points)
        print(len(visited_points))

# part1()