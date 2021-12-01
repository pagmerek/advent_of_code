with open('input') as f:
    data = f.read().split('\n\n')
    data[0] = data[0].split('\n')
    data[2] = data[2].split('\n')
    range_list = []
    for category in data[0]:
        category,ranges = category.split(':')
        first_range, sec_range = ranges.split('or')
        one, two = first_range.split('-')
        three, four = sec_range.split('-')
        range_list.append([ (int(one),int(two)), (int(three),int(four)) ] )
    invalid = []
    for ticket_vals in data[2][1:]:
        values = ticket_vals.split(',')
        for i in range(len(values)):
            found = False
            for j in range_list:
                if not ((not int(values[i]) in range(j[0][0],j[0][1]+1)) and (not int(values[i]) in range(j[1][0],j[1][1]+1))):
                        found = True
            if not found: invalid.append(values[i])
    invalid = [int(x) for x in invalid]
    print(sum(invalid))

