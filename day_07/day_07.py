class Node:
    left: object
    right: object
    value: str
    operand: str
    prev: object

    def __init__(self, value, operand):
        self.value = value
        self.operand = operand
        self.left = None
        self.right = None
        self.prev = None

    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node

    def get_prev(self):
        return self.prev

    def set_prev(self, node):
        self.prev = node


def construct_root(equation):
    nodes = []
    root = None
    for number in equation[1]:
        if nodes == []:
            n = Node(number, '')
            nodes.append(n)
            root = n
        else:
            new_nodes = []
            while len(nodes) > 0:
                n = nodes.pop()
                nn_l = Node(number, '+')
                nn_r = Node(number, '*')
                nn_l.set_prev(n)
                nn_r.set_prev(n)
                n.set_left(nn_l)
                n.set_right(nn_r)
                new_nodes.extend([nn_l, nn_r])
            nodes = new_nodes
    return root

def find_ends(nodes):
    ends = []
    while len(nodes) > 0:
        x = nodes.pop()
        l = x.get_left()
        r = x.get_right()
        if l:
            nodes.append(l)
        if r:
            nodes.append(r)
        if not (l and r):
            ends.append(x)
    return ends

def get_paths_from_ends(ends):
    paths = []
    for e in ends:
        current = e
        p = []
        while current.prev != None:
            p.append(current)
            current = current.prev
        p.append(current)
        p.reverse()
        paths.append(p)
    return paths

def parse_tree(root, goal):
    nodes = [root]
    ends = find_ends(nodes)
    paths = get_paths_from_ends(ends)

    for p in paths:
        total = 0
        for n in p:
            if n.operand == '+':
                total += int(n.value)
            elif n.operand == '*':
                total *= int(n.value)
            else:
                total = int(n.value)
        if total == goal:
            return True
    return False

def main():
    
    with open('puzzle7_input.txt') as f:
        lines = f.readlines()
        equations = []
        for l in lines:
            x = l.split(':')
            y = [int(p) for p in x[1].split()]
            equations.append((int(x[0]), y))
        roots = []
        for eq in equations:
            root = construct_root(eq)
            roots.append(root)
        
        total = 0
        for i in range(len(roots)):
            can_solve = parse_tree(roots[i], equations[i][0])
            if can_solve:
                total += int(equations[i][0])
        print('Total', total)
main()