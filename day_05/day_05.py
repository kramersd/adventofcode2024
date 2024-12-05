
input_file_name = 'puzzle5_input.txt'
# input_file_name = 'demo.txt'

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
part1()