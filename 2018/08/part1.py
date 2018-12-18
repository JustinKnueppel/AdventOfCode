class Node:
    def __init__(self, num_children, num_meta):
        self.num_children = num_children
        self.num_meta = num_meta
        self.children = []
        self.meta = []

    def add_child(self, node):
        self.children.append(node)

    def add_meta(self, meta):
        self.meta.append(meta)


def process_child(line, i):
    num_children = line[i]
    i += 1
    num_meta = line[i]
    i += 1
    child = Node(num_children, num_meta)
    for numc in range(num_children):
        c, i = process_child(line, i)
        child.add_child(c)
    for numm in range(num_meta):
        child.add_meta(line[i])
        i += 1
    return child, i

def sum_all_meta(child):
    total = 0
    for m in child.meta:
        total += m
    for c in child.children:
        total += sum_all_meta(c)
    return total

if __name__=='__main__':
    with open('day8inp.txt') as f:
        line = list(map(lambda x: int(x), f.readline().strip().split()))

    i = 0
    while i < len(line):
        root, i = process_child(line, i)

    print(sum_all_meta(root))

# 45210
