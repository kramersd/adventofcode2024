input_file_name = 'puzzle1_input.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        
        left = []
        right = []
        for l in lines:
            x = l.split()
            left.append(x[0].strip())
            right.append(x[1].strip())
        
        left.sort()
        right.sort()
        # print('Left', left)
        # print('Right', right)

        total = 0
        for idx in range(len(left)):
            total += abs(int(left[idx]) - int(right[idx]))
        print(total)


def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        
        left = []
        right = []
        for l in lines:
            x = l.split()
            left.append(x[0].strip())
            right.append(x[1].strip())
        
        num_count_map = {}
        for right_num in right:
            if right_num not in num_count_map:
                num_count_map[right_num] = 1
            else:
                num_count_map[right_num] += 1
        

        # print(num_count_map)
        total = 0
        for left_num in left:
            if left_num in num_count_map:
                # print(left_num)
                total = total + (int(left_num) * int(num_count_map[left_num]))
            else:
                total += 0
        print('Total', total)


part2()

