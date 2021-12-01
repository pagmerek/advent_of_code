import math
with open('input') as f:
    data_table = f.readlines()
    data_table = [x.strip() for x in data_table]
    acc = 0
    i = 0
    for iterat in range(len(data_table)):
        visited = [0]*len(data_table)
        i=0
        acc = 0
        while True:
            if i==len(data_table):
                    print(acc)
                    break
            if(visited[i]!=1):
                visited[i] = 1
                command, number = data_table[i].split()
                if command == 'acc':
                    acc += int(number)
                    i+=1
                elif command == 'jmp':
                    if i==iterat:
                        i+=1
                    else:
                        i+=(int(number))
                elif command == 'nop':
                    i+=1
            else:
                break
