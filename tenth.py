with open('input') as f:
    data_table = f.readlines()
    data_table = [int(x.strip()) for x in data_table]
    data_table.sort()
    print(data_table)
    jolt_dict = {}
    current_jolt = 0
    for i in data_table:
        if i >= current_jolt-3 and i <=current_jolt+3:
            print(i)
            if i-current_jolt not in jolt_dict:
                jolt_dict[abs(i - current_jolt)] = 1
            else:
                jolt_dict[abs(i - current_jolt)] += 1

            current_jolt = i
    jolt_dict[3]+=1
    print(jolt_dict)
    print(jolt_dict[1]*jolt_dict[3])      
