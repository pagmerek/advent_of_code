from itertools import chain, combinations
def powerset(table):
    xs = list(table)
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

with open('input') as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    memory = {}
    mask = ''
    for line in data:
        if(line[:4]=='mask'):
            mask = line[7:]
        else:
            line = line.split()
            index = int(line[0][4:-1])
            value = int(line[2])
            x_mem = []
            for i in range(len(mask)-1,-1,-1):
                if mask[i] == '1':
                    index |= (1<<(len(mask)-i-1))
                elif mask[i] == 'X':
                    x_mem.append(i)
            for subset in powerset(x_mem):
                for i in x_mem:
                    if i in subset:
                        index |= (1<<(len(mask)-i-1))
                    else:
                        index &= ~(1<<(len(mask)-i-1))
                memory[index] = value

    print(sum(memory.values()))                
