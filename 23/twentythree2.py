import cProfile
from collections import deque

def solve(raw):
    cups = [int(x) for x in raw]
    cups += list(range(10,10**6+1))
    array = dict()
    for k, v in enumerate(cups):
        array[v] = cups[(k+1)%1000000]
    current = 4
    for _ in range(10000000):
        splice = [array[current], array[array[current]], array[array[array[current]]]]
        nexttarget = (current-1)
        if not nexttarget: nexttarget = 1000000
        while nexttarget in splice:
            nexttarget = nexttarget-1
            if not nexttarget: nexttarget = 1000000
        array[current] = array[splice[2]]
        array[splice[2]] = array[nexttarget]
        array[nexttarget] = splice[0]
        current = array[current]
    return array[1], array[array[1]], array[1]*array[array[1]]

if __name__ == '__main__':
    with open('input') as f:
        raw = f.read()
    print(solve(raw))
