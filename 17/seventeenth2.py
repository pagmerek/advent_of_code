import numpy as np


def get_neighbours(coord, table):
    neighbour_table = np.empty((3, 3, 3), dtype='<U10')
    offset = [0]*4
    s_offset = [0]*4
    if coord[0] == 0:
        offset[0] = 1
    if coord[0] >= len(table)-1:
        s_offset[0] = 1
    if coord[1] == 0:
        offset[1] = 1
    if coord[1] >= len(table)-1:
        s_offset[1] = 1
    for i in range(2, len(coord)):
        if coord[i] == 0:
            offset[i] = 1
        if coord[i] >= len(table[0, 0])-1:
            s_offset[i] = 1
    for i in range(coord[0]-1+offset[0], coord[0]+2-s_offset[0]):
        for j in range(coord[1]-1+offset[1], coord[1]+2-s_offset[1]):
            for k in range(coord[2]-1+offset[2], coord[2]+2-s_offset[2]):
                neighbour_table[i % 3, j % 3, k % 3] += table[i, j, k][coord[3]-1+offset[3]:coord[3]+2-s_offset[3]]
    return neighbour_table


with open('input') as f:
    data = [x.strip() for x in f.readlines()]
    print(data)
    dimension = [[['.'*30]*30]*30]*30
    dimension = np.array(dimension, dtype='object')
    for i, line in enumerate(data):
        dimension[10,10,10+i] = dimension[10,10,10+i][:10] + line + dimension[10,10,10+i][10+len(line):]
    print(dimension[15])
    for cycle in range(6):
        temp_dim = dimension.copy()
        for i in range(len(dimension)):
            for j in range(len(dimension[i])):
                for k in range(len(dimension[i, j])):
                    for p in range(len(dimension[i, j, k])):
                        neighbours = get_neighbours((i, j, k, p), dimension)
                        active = 0
                        inactive = 0
                        for l in neighbours:
                            for n in l:
                                for z in n:
                                    active += z.count('#')
                                    inactive += z.count('.')

                        if(dimension[i, j, k][p] == '#'):
                            active -= 1
                            if active != 2 and active != 3:
                                temp_dim[i, j, k] = temp_dim[i, j, k][:p]+'.'+temp_dim[i, j, k][p+1:]
                        else:
                            inactive -= 1
                            if active == 3:
                                temp_dim[i, j, k] = temp_dim[i, j, k][:p]+'#'+temp_dim[i, j, k][p+1:]
        dimension = temp_dim
    count = 0
    for i in dimension:
        for j in i:
            for k in j:
                count += k.count('#')
    print(count)
