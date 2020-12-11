with open('input') as f:
    data_table = f.readlines()
    data_table = [x.strip() for x in data_table]
    while True:
        data_copy = data_table.copy()
        for i in range(len(data_table)):
            for j in range(len(data_table[i])):
                neighbours = []
                if i+1<len(data_table):
                    neighbours.append(data_copy[i+1][j])
                    if j+1<len(data_table[i]):
                        neighbours.append(data_copy[i+1][j+1])
                    if j-1>=0:
                        neighbours.append(data_copy[i+1][j-1])
                if i<len(data_table):
                    if j+1<len(data_table[i]):
                        neighbours.append(data_copy[i][j+1])
                    if j-1>=0:
                        neighbours.append(data_copy[i][j-1])
                if i-1>=0:
                    neighbours.append(data_copy[i-1][j])
                    if j+1<len(data_table[i]):
                        neighbours.append(data_copy[i-1][j+1])
                    if j-1>=0:
                        neighbours.append(data_copy[i-1][j-1])
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
            