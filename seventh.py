def count_bags(name):
    n = 0
    if name in bag_dict:
        for bag in bag_dict[name]:
                n+=bag[0]*(1+count_bags(bag[1]))                              
    return n

with open('input') as f:
    data_table = f.readlines()
    data_table = [x.strip() for x in data_table]
    bag_dict = {}
    for line in data_table:
        line = line.split()
        current_color = line[0] + ' ' + line[1]
        for i in range(len(line)):
            if line[i] in "123456789":
                bag_tuple = (int(line[i]),line[i+1]+ ' '+line[i+2])
                if  str(current_color) not in bag_dict :
                    bag_dict[current_color] = []
                    bag_dict[current_color].append(bag_tuple)
                else:
                    bag_dict[current_color].append(bag_tuple)
    counter = count_bags('shiny gold')
    print(counter)
    