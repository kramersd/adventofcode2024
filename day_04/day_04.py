import re
# input_file_name = 'puzzle4_input.txt'
input_file_name = 'demo.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        
        aaa = []

        rows = []
        for l in lines:
            r = []
            l = l.strip()
            for letter in l:
                r.append(letter)
            rows.append(r)
        
        print(len(rows), len(rows[0]))
        forward_rows = []
        backward_rows = []
        for r in rows:
            x = ''
            y = ''
            for i in r:
                x += i
                y += i
            forward_rows.append(x)
            backward_rows.append(y[::-1])
        print(forward_rows)
        print(backward_rows)

        forward_cols = []
        backward_cols = []

        for j in range(len(rows[0])):
            x = ''
            y = ''
            for i in range(len(rows)):
                x += rows[i][j]
                y += rows[i][j]
            forward_cols.append(x)
            backward_cols.append(y[::-1])
        print(forward_cols)
        print(backward_cols)

        forward_diag = []
        backward_diag = []
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                if i + 4 < len(rows) and j + 4 < len(rows[0]):
                    x = ''
                    for k in range(4):
                        x += rows[i + k][j + k]
                    forward_diag.append(x)
                if i - 4 > 0 and j - 4 > 0:
                    y = ''
                    for k in range(4):
                        y += rows[i - k][j - k]
                    backward_diag.append(y)
        
        all = forward_cols + backward_cols + forward_rows + backward_rows + forward_diag + backward_diag

        pattern = r"XMAS"
        prog = re.compile(pattern)
        total = 0
        for a in all:
            print('A', a)
            result = prog.findall(a)
            if len(result) > 0:
                print(result)
                total += len(result)
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

part1()