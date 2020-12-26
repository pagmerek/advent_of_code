import copy

def count_adj_black(x, y, tile_set):
    count_table = []
    if x+2 < 300:
        count_table.append(tile_set[y][x+2])
    if x-2 >= 0:
        count_table.append(tile_set[y][x-2])
    if y-1 >= 0 and x+1 < 300:
        count_table.append(tile_set[y-1][x+1])
    if y-1 >= 0 and x-1 >= 0:
        count_table.append(tile_set[y-1][x-1])
    if y+1 < 300 and x-1 >= 0:
        count_table.append(tile_set[y+1][x-1])
    if y+1 < 300 and x+1 < 300:
        count_table.append(tile_set[y+1][x+1])
    return sum(count_table)


if __name__ == '__main__':
    with open('input') as f:
        data = f.read().split('\n')
    tile_set = [[0 for _ in range(300)] for _ in range(300)]
    black = 0
    for line in data:
        curr_x = 150
        curr_y = 150
        i = 0
        while i < len(line):
            if line[i] == 'e':
                curr_x += 2
            elif line[i] == 'w':
                curr_x -= 2
            elif line[i:(i+2)] == 'nw':
                curr_x -= 1
                curr_y -= 1
                i += 1
            elif line[i:(i+2)] == 'ne':
                curr_x += 1
                curr_y -= 1
                i += 1
            elif line[i:(i+2)] == 'sw':
                curr_x -= 1
                curr_y += 1
                i += 1
            elif line[i:(i+2)] == 'se':
                curr_x += 1
                curr_y += 1
                i += 1
            i += 1
        tile_set[curr_y][curr_x] = (tile_set[curr_y][curr_x]+1) % 2
    for _ in range(100):
        new_tile = copy.deepcopy(tile_set)
        for k, row in enumerate(tile_set):
            z = k % 2
            for j in range(z,len(row),2):
                count = count_adj_black(j, k, tile_set)
                if tile_set[k][j] == 0:
                    if count == 2:
                        new_tile[k][j] = 1
                else:
                    if count == 0 or count > 2:
                       new_tile[k][j] = 0
        tile_set = new_tile
    for row in tile_set:
        for i in range(0,len(row)):
            if row[i] == 1:
                black += 1
    print(black)
