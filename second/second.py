with open('input') as f:
    input_data = f.readlines()
    input_data = [x.strip() for x in input_data] 
    counter = 0
    for i in input_data:
        line = i.split()
        low, high = line[0].split('-')
        char = line[1][0]
        passwrd = line[2]
        chardict = {}
        for i in passwrd:
            if i in chardict:
                chardict[i] += 1
            else:
                chardict[i] = 1
        
        if char in chardict and chardict[char] <= int(high) and chardict[char] >= int(low):
            counter+=1
    print(counter)

with open('input') as f:
    input_data = f.readlines()
    input_data = [x.strip() for x in input_data] 
    counter = 0
    for i in input_data:
        line = i.split()
        low, high = line[0].split('-')
        char = line[1][0]
        passwrd = line[2]
        if (passwrd[int(low)-1] == char) ^ (passwrd[int(high)-1]==char):
            counter+=1
    print(counter)
        