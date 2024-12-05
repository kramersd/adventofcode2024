
input_file_name = 'puzzle5_input.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        
        total = 0
        for l in lines:
            print(l)