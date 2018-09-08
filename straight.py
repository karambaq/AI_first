from collections import deque

from time_dec import time_dec_seconds
from state import State


@time_dec_seconds
def find_leaf(a, b):
    leafs = [State(a)]
    seen = set()

    while True:
        new_leafs = []

        for i in leafs:
            cur_value = i.value * 2
            if cur_value not in seen and cur_value <= b:
                new_leafs.append(State(cur_value, '*2', i))
                seen.add(cur_value)
            if cur_value == b:
                print(f"Visited nodes count: {len(seen)}")
                return new_leafs[-1]

            cur_value = i.value + 3
            if cur_value not in seen:
                new_leafs.append(State(cur_value, '+3', i))
                seen.add(cur_value)
            if cur_value == b:
                print(f"Visited nodes count: {len(seen)}")
                return new_leafs[-1]

        leafs = new_leafs


#@time_dec_seconds
def find_seq(leaf):
    seq = [leaf]
    cur = leaf
    while True:
        parent = cur.parent
        if parent is None:
            return seq[::-1]
        seq.append(parent)
        cur = parent

a = int(input('Input a: '))
b = int(input('Input b: '))

leaf = find_leaf(a, b)
op_seq = find_seq(leaf)
print(op_seq)
print(len(op_seq))
