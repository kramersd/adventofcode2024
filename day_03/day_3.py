import re
input_file_name = 'puzzle3_input.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        
        total = 0
        for l in lines:
            l = l.strip()
            pattern = r"mul\(\d*,\d*\)"
            prog = re.compile(pattern)
            result = prog.findall(l)

            if len(result) > 0:
                for r in result:
                    p2 = r"\d+"
                    prog2 = re.compile(p2)
                    result2 = prog2.findall(r)

                    numbers = [int(num) for num in result2]
                    total += (numbers[0] * numbers[1])
        print('Total', total)

    
def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        
        total = 0
        enabled = True # Only enabled at the start, not enabled at the start of each line by default.
        for l in lines:
            l = l.strip()
            pattern = r"mul\(\d*,\d*\)|do\(\)|don\'t\(\)"
            prog = re.compile(pattern)
            result = prog.findall(l)

            if len(result) > 0:
                for r in result:
                    if enabled:
                        if r in ('do()'):
                            x = 5
                        elif r in ('don\'t()'):
                            enabled = False
                        else:
                            p2 = r"\d+"
                            prog2 = re.compile(p2)
                            result2 = prog2.findall(r)
                            numbers = [int(num) for num in result2]
                            total += (numbers[0] * numbers[1])
                           
                    else:
                        if r in ('do()'):
                            enabled = True 
        print('Total', total)

part2()