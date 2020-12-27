with open('input') as f:
    data_table = f.readlines()
    data_table = [x.strip() for x in data_table]
    while True:
        data_copy = data_table.copy()
        for i in range(len(data_table)):
            for j in range(len(data_table[i])):
                if data_table[i][j] != '.':
                    neighbours = []
                    left = [i,j]
                    while left[1] > 0:
                        left[1] -= 1
                        if data_table[left[0]][left[1]] != '.':
                            neighbours.append(data_copy[left[0]][left[1]])
                            break
                    right = [i,j]
                    while right[1] < len(data_table[right[0]])-1:
                        right[1] += 1
                        if data_table[right[0]][right[1]] != '.':
                            neighbours.append(data_copy[right[0]][right[1]])
                            break                       
                    up = [i,j]
                    while up[0] > 0:
                        up[0] -= 1
                        if data_table[up[0]][up[1]] != '.':
                            neighbours.append(data_copy[up[0]][up[1]])
                            break
                    down = [i,j]
                    while down[0] < len(data_table)-1:
                        down[0] += 1
                        if data_table[down[0]][down[1]] != '.':
                            neighbours.append(data_copy[down[0]][down[1]])
                            break
                    lup = [i,j]     
                    while lup[1] > 0 and lup[0] > 0:
                        lup[1] -= 1
                        lup[0] -= 1
                        if data_table[lup[0]][lup[1]] != '.':
                            neighbours.append(data_copy[lup[0]][lup[1]])
                            break
                    ldown = [i,j]       
                    while ldown[1] > 0 and ldown[0] < len(data_table)-1:
                        ldown[1] -= 1
                        ldown[0] += 1
                        if data_table[ldown[0]][ldown[1]] != '.':
                            neighbours.append(data_copy[ldown[0]][ldown[1]])
                            break
                    rup = [i,j]    
                    while rup[1] < len(data_table[rup[0]])-1 and rup[0] > 0:
                        rup[1] += 1
                        rup[0] -= 1
                        if data_table[rup[0]][rup[1]] != '.':
                            neighbours.append(data_copy[rup[0]][rup[1]])
                            break
                    rdown = [i,j]    
                    while rdown[1] < len(data_table[rdown[0]])-1 and rdown[0] < len(data_table)-1:
                        rdown[1] += 1
                        rdown[0] += 1
                        if data_table[rdown[0]][rdown[1]] != '.':
                            neighbours.append(data_copy[rdown[0]][rdown[1]])
                            break                      
                    taken_count = neighbours.count('#')
                    if data_table[i][j] == 'L' and '#' not in neighbours:
                        data_table[i] = data_table[i][:j] + '#' + data_table[i][j+1:]
                    elif data_table[i][j] == '#' and taken_count >= 5:
                        data_table[i] = data_table[i][:j] + 'L' + data_table[i][j+1:]
        if data_table == data_copy: 
            break
    counter = 0
    for i in data_table:
        counter+=i.count('#')
    print(counter)
            