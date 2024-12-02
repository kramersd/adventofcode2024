input_file_name = 'puzzle2_input.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        total = 0
        for l in lines:
            x = l.split()
            x = [int(m) for m in x]
            print('Split', x)

            prev_num = x[0]
            flag = None
            should_increment = True

            for i in range(1, len(x)):
                print('Prev num, current_num', prev_num, x[i])
                if abs(prev_num - x[i]) > 3:
                    print('Unsafe', 'greater > 3')
                    prev_num = x[i]
                    should_increment = False
                    break
                elif (prev_num - x[i] == 0):
                    print('Unsafe', '== 0')
                    prev_num = x[i]
                    should_increment = False
                    break

                if flag == None:
                    if (prev_num - x[i] < 0):
                        flag = 'decrease'
                        prev_num = x[i]
                    elif (prev_num - x[i] > 0):
                        flag = 'increase'
                        prev_num = x[i]
                else:
                    if flag == 'decrease' and (prev_num - x[i] > 0):
                        print('Unsafe', 'Changed to increase')
                        prev_num = x[i]
                        should_increment = False
                        break
                    elif flag == 'increase' and (prev_num - x[i] < 0):
                        print('Unsafe', 'Changed to decrease')
                        prev_num = x[i]
                        should_increment = False
                        break
                    else:
                        prev_num = x[i]
                
            if should_increment:
                print('Safe', x)
                total += 1
        print('Total', total)



def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        total = 0
        for l in lines:
            x = l.split()
            x = [int(m) for m in x]
            n = x

            permutations = []
            for i in range(len(x)):
                aaa = []
                for j in range(len(x)):
                    if i != j:
                        aaa.append(x[j])
                permutations.append(aaa)

            for p in permutations:
                x = p
                prev_num = x[0]
                flag = None
                should_increment = True

                for i in range(1, len(x)):
                    
                    if abs(prev_num - x[i]) > 3:
                        prev_num = x[i]
                        should_increment = False
                        break
                    elif (prev_num - x[i] == 0):
                        prev_num = x[i]
                        should_increment = False
                        break

                    if flag == None:
                        if (prev_num - x[i] < 0):
                            flag = 'decrease'
                            prev_num = x[i]
                        elif (prev_num - x[i] > 0):
                            flag = 'increase'
                            prev_num = x[i]
                    else:
                        if flag == 'decrease' and (prev_num - x[i] > 0):
                            prev_num = x[i]
                            should_increment = False
                            break
                        elif flag == 'increase' and (prev_num - x[i] < 0):
                            prev_num = x[i]
                            should_increment = False
                            break
                        else:
                            prev_num = x[i]
                if should_increment:
                    total += 1
                    break
        print('Total', total)


part2()

