
def find_path(table,paths_from, i):
    count = 0
    if i < len(table)-1:
        if table[i] not in paths_from:
            if i+1<len(table) and table[i] >= table[i+1] - 3:
                count += find_path(table,paths_from,i+1)
            if i+2<len(table) and table[i] >= table[i+2] - 3:
                count += find_path(table,paths_from,i+2)
            if i+3<len(table) and table[i] >= table[i+3] - 3:
                count += find_path(table,paths_from,i+3)
            paths_from[table[i]] = count 
        else:
            count += paths_from[table[i]]
    else:
        count = 1
    return count
    
with open('input') as f:
    data_table = f.readlines()
    data_table = [int(x.strip()) for x in data_table]
    data_table.sort()
    data_table.append(data_table[-1]+3)
    data_table.insert(0,0)
    paths_from = {}
    print(data_table)
    print(find_path(data_table,paths_from,0))
    print(paths_from)

    