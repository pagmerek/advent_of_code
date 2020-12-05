import math
with open('input') as f:
    data_input = f.readlines()
    data_input = [x.strip() for x in data_input]
    row_table = []
    col_table =[]
    for i in data_input:
        low_row=0
        high_row = 127
        low_col = 0
        high_col=7
        instruction = i.split()
        for i in instruction[0]:
            if i == 'F': 
                high_row=(high_row+low_row)//2
            if i == 'B':  
                low_row=math.ceil((low_row+high_row)/2)
            if i=='R':
                low_col=math.ceil((high_col+low_col)/2)
            if i =='L':
                high_col = (high_col+low_col)//2
        if(high_row == low_row and high_col == low_col):
             row_table.append((low_row,low_col))
    row_table.sort()
    seat = (0,0)
    found_num = False
    for i in range(128):
        for j in range(8):
            if seat in row_table:
                found_num = True
                seat = (i,j)
            elif seat not in row_table and found_num == False:
                seat = (i,j)
            else:
                print(seat[0]*8 + seat[1])
                break