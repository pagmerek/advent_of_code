from collections import deque

def solve(raw):
    cups = [int(x) for x in raw]
    cups += list(range(10,10**6+1))
    print(len(cups))
    current_index = 0
    cups = deque(cups)
    for i in range(10000000):
        if i % 1000 == 0:
            print(i/10000000 * 100,"%")
        current_cup = cups[current_index % len(cups)]
        pick_up = []
        if(current_index% len(cups) > len(cups)-4):
            while(current_index% len(cups) != len(cups)-4):
                cups.rotate(-1)
                current_index -= 1
        index = current_index % len(cups)+1
        for _ in range(3):
            element = cups[index]
            del cups[index]
            pick_up.append(element)
        destination = current_cup - 1 if current_cup != 1 else max(cups)
        while(destination in pick_up):
            destination = (destination-1)
            if destination == 0:
                destination = max(cups)
        destination_index = cups.index(destination)
        for i in reversed(pick_up):
            cups.insert(destination_index+1,i)
        if(destination_index < current_index % len(cups)):
            current_index += 3
        current_index += 1
    while(cups[0] != 1):
        cups.rotate(-1)
    print(cups[1]*cups[2])

if __name__ == '__main__':
    with open('23/input') as f:
        raw = f.read()
    print(solve(raw))