from collections import deque

from time_dec import time_dec_seconds
from state import State


def find_leaf_in_set_of_states(states, leaf):
    leaf_value = leaf.value
    for s in states:
        if s.value == leaf_value:
            return s

@time_dec_seconds
def find_leaf(a, b):
    straight_leafs = [State(a)]
    reverse_leafs = [State(b)]
    straight_seen = set()
    reverse_seen = set()
    straight_tree = []

    while True:
        new_leafs_straight = []
        new_leafs_reverse = []

        gen_straight_way(straight_seen, straight_leafs, new_leafs_straight, straight_tree, a, b)
        gen_back_way(reverse_seen, reverse_leafs, new_leafs_reverse, a, b)
        
        tree_vals = set(node.value for node in new_leafs_reverse) 
        straight_way = [node for node in straight_tree if node.value in tree_vals]
        
        if straight_way:
            back_way = find_leaf_in_set_of_states(new_leafs_reverse, straight_way[0])
            print(f"Visited nodes count: {len(reverse_seen) + len(straight_seen)}")
            return straight_way[0], back_way

        straight_leafs = new_leafs_straight
        reverse_leafs = new_leafs_reverse

def gen_straight_way(seen, leafs, new_leafs, tree, a, b):
    new_leafs = []
    for i in leafs:
        cur_value = i.value * 2
        if cur_value not in seen and cur_value <= b:
            new_leafs.append(State(cur_value, '*2', i))
            seen.add(cur_value)

        cur_value = i.value + 5
        if cur_value not in seen and cur_value <= b:
            new_leafs.append(State(cur_value, '+5', i))
            seen.add(cur_value)

        cur_value = i.value * 3
        if cur_value not in seen and cur_value <= a:
            new_leafs.append(State(cur_value, '*3', i))
            seen.add(cur_value)

        cur_value = i.value - 7
        if cur_value not in seen and cur_value >= a:
            new_leafs.append(State(cur_value, '-7', i))
            seen.add(cur_value)

        cur_value = i.value + 3
        if cur_value not in seen and cur_value <= b:
            new_leafs.append(State(cur_value, '+3', i))
            seen.add(cur_value)

        cur_value = i.value - 2
        if cur_value not in seen and cur_value >= a:
            new_leafs.append(State(cur_value, '-2', i))
            seen.add(cur_value)
        

        #straight_tree = np.append(straight_tree, new_leafs_straight)
        tree.extend(new_leafs)

def gen_back_way(seen, leafs, new_leafs, a, b):
    for i in leafs:
        val = i.value
        if val % 2 == 0:
            cur_value = val / 2
            if cur_value not in seen and cur_value >= a:
                new_leafs.append(State(cur_value, '/2', i))
                seen.add(cur_value)

        cur_value = i.value - 5
        if cur_value not in seen and cur_value >= a:
            new_leafs.append(State(cur_value, '-5', i))
            seen.add(cur_value)

        if val % 3 == 0:
            cur_value = i.value / 3
            if cur_value not in seen and cur_value >= a:
                new_leafs.append(State(cur_value, '/3', i))
                seen.add(cur_value)

        cur_value = i.value - 3
        if cur_value not in seen and cur_value >= a:
            new_leafs.append(State(cur_value, '-3', i))
            seen.add(cur_value)

        cur_value = i.value + 7
        if cur_value not in seen and cur_value <= b:
            new_leafs.append(State(cur_value, '+7', i))
            seen.add(cur_value)

        cur_value = i.value + 2
        if cur_value not in seen and cur_value <= b:
            new_leafs.append(State(cur_value, '+2', i))
            seen.add(cur_value)

#@time_dec_seconds
def find_seq(leaf, way):
    seq = [leaf]
    cur = leaf
    while True:
        parent = cur.parent
        if parent is None:
            if way == 'straight':
                return seq[::-1]
            else:
                return seq
        seq.append(parent)
        cur = parent

a = int(input('Input a: '))
b = int(input('Input b: '))

ways = find_leaf(a, b)
straight_way = find_seq(ways[0], 'straight')
back_way = find_seq(ways[1], 'back')
for s in back_way[:-1]:
    s.reverse_op()
way = straight_way + back_way
print(way)
print(len(way))
