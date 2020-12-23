

if __name__ == '__main__':
    with open('input') as f:
        raw = f.read()
    cups = [int(x) for x in raw]
    current_index = 0
    for i in range(100):
        current_cup = cups[current_index%len(cups)]
        pick_up = []
        if(cups.index(current_cup) > len(cups)-4):
            while(cups.index(current_cup)!=len(cups)-4):
                cups.append(cups.pop(0))
                current_index -= 1
        index = current_index%len(cups)+1
        for z in range(3):
            element = cups.pop(index)
            pick_up.append(element)
        destination = current_cup - 1 if current_cup!=1 else max(cups)
        while(destination in pick_up):
            destination = (destination-1)
            if destination == 0:
                destination = max(cups)
        cups[cups.index(destination)+1:cups.index(destination)+1] = pick_up
        if(cups.index(destination)< current_index%len(cups)): current_index+=3
        current_index += 1
    while(cups[0]!=1):
        cups.append(cups.pop(0))
    print(cups)
