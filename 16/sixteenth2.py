def find(val, table):
    return not ((not int(val) in range(table[1][0][0],table[1][0][1]+1)) and 
                (not int(val) in range(table[1][1][0],table[1][1][1]+1)))

with open('input') as f:
    data = f.read().split('\n\n')
    data[0] = data[0].split('\n')
    data[2] = data[2].split('\n')
    my_ticket = data[1].split(':\n')[1].split(',')
    for i in range(1,len(data[2])):
        data[2][i] = data[2][i].split(',')
    data[2].append(my_ticket)
    range_list = []
    for category in data[0]:
        category,ranges = category.split(':')
        first_range, sec_range = ranges.split('or')
        one, two = first_range.split('-')
        three, four = sec_range.split('-')
        range_list.append([category,((int(one),int(two)), (int(three),int(four)))])
    invalid = []
    for value in data[2][1:]:
        print(value)
        for i in range(len(value)):
            found = False
            for j in range_list:
                if(find(value[i],j)): found = True
            if not found: 
                data[2].remove(value)

    valid_categories = []
    for num in range(len(my_ticket)):
        valid_cat = []
        for rang in range_list:
            found_bad = False
            for i in range(1,len(data[2])):
                if not find(data[2][i][num],rang): found_bad = True
            if not found_bad:
                valid_cat.append(rang[0])
        valid_categories.append([len(valid_cat), (valid_cat,num)])
    anwser_table = {}
    for i in range(len(valid_categories)):
        to_del = ''
        for i in valid_categories:
            if i[0] == 1:
                to_del = i
        if to_del:
            if 'departure' in to_del[1][0][0]:
                anwser_table[to_del[1][0][0]] = to_del[1][1]
            delete = to_del[1][0][0]
            for j in range(0,len(valid_categories)):
                if delete in valid_categories[j][1][0]:
                    valid_categories[j][1][0].remove(delete)
                    valid_categories[j][0] -= 1
    mult = 1
    for i in anwser_table:
        mult *= int(my_ticket[anwser_table[i]])
    print(mult)