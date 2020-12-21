import numpy as np


def parse(raw):
    data = raw.split('\n\n')
    puzzles = []
    tiles = []
    for d in data:
        puzzle = np.array([[0 for f in range(10)] for s in range(10)],dtype='str')
        d = d.split('\n')
        tiles.append(d[0])
        puzzle_data = d[1:]
        for ind, val in enumerate(puzzle_data):
            for indx, valx in enumerate(val):
                puzzle[ind,indx] = valx
        puzzles.append(puzzle)
    return(tiles, puzzles)


if __name__ == '__main__':
    with open('input') as f:
        data = f.read()
    tiles, puzzles = parse(data)
    puzzles = np.array(puzzles)
    print(puzzles)
    print(tiles)
