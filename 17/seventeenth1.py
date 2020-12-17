import numpy as np

def get_neighbours(coord, table):
    neighbour_table = np.empty((3,3),dtype='<U10')
    offset = [0]*3
    s_offset = [0]*3
    if coord[0] == 0: offset[0] = 1
    if coord[0] >= len(table)-1: s_offset[0] = 1
    for i in range(1,len(coord)):
        if coord[i] == 0: offset[i] = 1
        if coord[i] >= len(table[0])-1: s_offset[i] = 1
    for i in range(coord[0]-1+offset[0], coord[0]+2-s_offset[0]):
        for j in range(coord[1]-1+offset[1],coord[1]+2-s_offset[1]):
            neighbour_table[i%3,j%3] += table[i,j][coord[2]-1+offset[2]:coord[2]+2-s_offset[2]]
    return neighbour_table


with open('input') as f:
    data = [x.strip() for x in f.readlines()]
    for i in range(len(data)):
        data[i] += '.'
        data[i] = '.' + data[i]
    data.append('.'*(len(data[0])))
    data.insert(0,'.'*(len(data[0])))
    dimension = [['.'*len(data[0])]*len(data[0])]*3
    dimension = np.array(dimension,dtype='object')
    dimension[1]=data
    for cycle in range(6):
        temp_dim = dimension.copy()
        for i in range(len(dimension)):
            for j in range(len(dimension[i])):
                for k in range(len(dimension[i][j])):
                    neighbours = get_neighbours((i,j,k), dimension)
                    active = 0
                    inactive = 0
                    for l in neighbours:
                        for n in l:
                            active += n.count('#')
                            inactive += n.count('.')
                    if(dimension[i,j][k] == '#'):
                        active -= 1
                        if active != 2 and active != 3:
                            temp_dim[i,j] = temp_dim[i,j][:k]+'.'+temp_dim[i,j][k+1:]
                    else: 
                        inactive -= 1
                        if active == 3:
                            temp_dim[i,j] = temp_dim[i,j][:k]+'#'+temp_dim[i,j][k+1:]
        dimension = temp_dim
        for i in range(len(dimension)):
            for j in range(len(dimension[i])):
                dimension[i,j] = '.' + dimension[i,j]
                dimension[i,j] += '.'
        new_row = np.array(['.'*len(dimension[0,0])]*len(dimension[0]))
        dimension = np.vstack((dimension,new_row))
        dimension = np.insert(dimension,0,new_row,0)
        new_col = np.array(['.'*len(dimension[0,0])]*len(dimension))
        dimension = np.column_stack((dimension,new_col))
        dimension = np.insert(dimension,0,new_col,1)
    count = 0
    for i in dimension:
        for j in i:
            count += j.count('#')
    print(count)
