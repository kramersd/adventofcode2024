def prep_memo(memo):
    for i in range(2, 10000000):
        if len(str(i)) % 2 == 0:
            s = str(i)
            middle = int(len(s) / 2)
            ns_1 = int(s[:middle])
            ns_2 = int(s[middle:])
            memo[i] = [ns_1, ns_2]
        else:
            memo[i] = [2024 * i]
    return memo

def update_map(next_stones_map, entry, csm_value):
    if entry in next_stones_map:
        next_stones_map[entry] += csm_value
    else:
        next_stones_map[entry] = csm_value

def main():
    with open('puzzle11_input.txt') as f:
        lines = f.readlines()
        stones = []
        stones_map = {}
        for l in lines:
            stones = [int(i) for i in l.split()]
            for s in stones:
                if int(s) not in stones_map:
                    stones_map[int(s)] = 1
    memo = {}
    print('Start prep')
    memo = prep_memo(memo)
    print('End prep')

    blinking_times = 25   # Part 1
    # blinking_times = 75 # Part 2
    memo[0] = [1]
    memo[1] = [2024]

    current_stones_map = stones_map
    print(current_stones_map)

    for i in range(blinking_times):
        next_stones_map = {}
        for cs in current_stones_map.keys():
            if cs in memo:
                new_entries = memo[cs]
                for ne in new_entries:
                    update_map(next_stones_map, ne, current_stones_map[cs])
            else:
                if len(str(cs)) % 2 == 0:
                    s = str(cs)
                    middle = int(len(s) / 2)
                    ns_1 = int(s[:middle])
                    ns_2 = int(s[middle:])

                    update_map(next_stones_map, ns_1, current_stones_map[cs])
                    update_map(next_stones_map, ns_2, current_stones_map[cs])
                    memo[cs] = [ns_1, ns_2]
                else:
                    update_map(next_stones_map, (2024 * cs), current_stones_map[cs])
                    memo[cs] = [2024 * cs]
        current_stones_map = next_stones_map
        # print('I finish', i)
    print('Total', sum(current_stones_map.values()))

main()