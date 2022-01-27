with open('input') as f:
    data_table = f.readlines()
    data_table = [x.strip() for x in data_table] 
    b = 0
    counter = [0,0,0,0,0]
    for i in range(len(data_table)):
        if data_table[i][b%(len(data_table[i]))]=='#': counter[0]+=1
        b+=3
    b = 0
    for i in range(len(data_table)):
        if data_table[i][b%(len(data_table[i]))]=='#': counter[1]+=1
        b+=5
    b=0
    for i in range(len(data_table)):
        if data_table[i][b%(len(data_table[i]))]=='#': counter[2]+=1
        b+=7
    b=0
    for i in range(0,len(data_table),2):
        if data_table[i][b%(len(data_table[i]))]=='#': counter[3]+=1
        b+=1
    b=0
    for i in range(len(data_table)):
        if data_table[i][b%(len(data_table[i]))]=='#': counter[4]+=1
        b+=1
    
    print(counter)
    print(counter[0]*counter[1]*counter[2]*counter[3]*counter[4])
