
with open('input') as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    memory = [0]*10000000
    mask = ''
    for line in data:
        if(line[:4]=='mask'):
            mask = line[7:]
            print(mask)
        else:
            line = line.split()
            index = int(line[0][4:-1])
            value = int(line[2])
            for i in range(len(mask)-1,-1,-1):
                if mask[i] == '1':
                    value |= (1<<(len(mask)-i-1))
                elif mask[i] == '0':
                    value &= ~(1<<(len(mask)-i-1))
            memory[index]=value    
    print(sum(memory))                
