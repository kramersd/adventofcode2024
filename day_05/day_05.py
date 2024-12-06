from copy import deepcopy

# input_file_name = 'puzzle5_input.txt'
input_file_name = 'demo.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        
        rules = []
        updates = []
        for l in lines:
            l = l.strip()

            if '|' in l:
                a = l.split('|')
                rules.append((a[0], a[1]))
            elif l != '':
                b = []
                c = l.split(',')
                for d in c:
                    b.append(d)
                updates.append(b)
        print('Rules', rules)
        print('Updates', updates)

        overall = {}
        for ui in range(len(updates)):
            overall[ui] = {
                'rules': [],
                'update': updates[ui]
            }

            for ri in range(len(rules)):
                idx_r0 = []
                idx_r1 = []
                for i in range(len(updates[ui])):
                    if updates[ui][i] == rules[ri][0]:
                        idx_r0.append(i)
                    elif updates[ui][i] == rules[ri][1]:
                        idx_r1.append(i)

                s = []
                if len(idx_r0) == 0 or len(idx_r1) == 0:
                    status = True
                    s.append(status)
                else:
                    for r0 in idx_r0:
                        status = False
                        for r1 in idx_r1:
                            if r0 < r1:
                                status = True
                                break
                        s.append(status)

                overall[ui]['rules'].append({
                    'rule': rules[ri],
                    'statuses': s
                })
        
        valid_updates = []
        for v in overall.values():
            is_valid = True
            for r in v['rules']:
                for x in r['statuses']:
                    if x == False:
                        is_valid = False
            if is_valid:
                valid_updates.append(v['update'])
        
        print('Valid Updates')
        total  = 0
        for vu in valid_updates:
            print(vu)
            mid_idx = ((len(vu) // 2))
            total += int(vu[mid_idx])
        
        print('Total', total)


def get_rule_positions_in_update(rule, update):
    idx_r0 = []
    idx_r1 = []
    for i in range(len(update)):
        # Find the positions of all r0 numbers in the specific update
        if update[i] == rule[0]:
            idx_r0.append(i)
        # Find the positions of all r1 numbers in the specific update
        elif update[i] == rule[1]:
            idx_r1.append(i)
    return (idx_r0, idx_r1)


def evaluate_rule_for_an_update(rule, update):
    idx_r0, idx_r1 = get_rule_positions_in_update(rule, update)

    s = []
    if len(idx_r0) == 0 or len(idx_r1) == 0:
        status = True
        s.append(status)
    else:
        for r0 in idx_r0:
            status = False
            for r1 in idx_r1:
                if r0 < r1:
                    status = True
                    break
            s.append(status)
    return s

def generate_permutations():
    print()

def fix_rule(invalid_update, rule_being_violated, rules):
    iu = deepcopy(invalid_update)
    idx_r0, idx_r1 = get_rule_positions_in_update(rule_being_violated['rule'], invalid_update['update'])

    iu['update'].pop(idx_r1[0])
    # print('IU to fix', iu['update'])
    permutations = []
    for i in range(len(iu['update']) + 1):
        temp =  deepcopy(iu['update'])
        temp.insert(i, invalid_update['update'][idx_r1[0]])
        permutations.append(
           temp
        )
    
    # print('Perms', permutations)
    for p in permutations:
        print('>Current perm', p)
        valid_permutation = True
        for ri in range(len(rules)):
            statuses = evaluate_rule_for_an_update(rules[ri], p)
            print('Statuses', rules[ri], statuses)
            if statuses[0] == False:
                valid_permutation = False
                print('Invalid perm', 'violates', rules[ri])
                break
        if valid_permutation == True:
            print('Valid perm', p)
            invalid_update['update'] = p
            return

def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        
        rules = []
        updates = []
        for l in lines:
            l = l.strip()

            if '|' in l:
                a = l.split('|')
                rules.append((a[0], a[1]))
            elif l != '':
                b = []
                c = l.split(',')
                for d in c:
                    b.append(d)
                updates.append(b)
        print('Rules', rules)
        # print('Updates', updates)

        overall = {}

        # Iterate over all the updates
        for ui in range(len(updates)):
            overall[ui] = {
                'rules': [],
                'update': updates[ui]
            }
            # Iterate over all the rules, each rule is in format r0,r1
            for ri in range(len(rules)):
                statuses = evaluate_rule_for_an_update(rules[ri], updates[ui])
                overall[ui]['rules'].append({
                    'rule': rules[ri],
                    'statuses': statuses
                })
        
        invalid_updates = []
        for v in overall.values():
            is_valid = True
            for r in v['rules']:
                for x in r['statuses']:
                    if x == False:
                        is_valid = False
            if is_valid == False:
                invalid_updates.append(v)
        
        print('Invalid Updates')
        new_updates = []
        for iu in invalid_updates:
            print('===============>IU', iu['update'])
            
        
        total  = 0
        print('New Updates')
        for nu in new_updates:
            print(nu)
            mid_idx = ((len(nu) // 2))
            total += int(nu[mid_idx])
        
        print('Total', total)
        print()
        
# part1()
part2()