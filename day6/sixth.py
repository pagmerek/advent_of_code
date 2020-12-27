with open('input') as f:
    input_data = f.read()
    input_table = input_data.split('\n\n')
    count = 0
    for i in input_table:
        letter_dict = {} 
        i = i.split('\n')
        print(i , '\n')
        for j in i:
            for k in j:
                if k not in letter_dict:
                    letter_dict[k] = 1
                else:
                    letter_dict[k]+=1
        for value in letter_dict:
            if letter_dict[value] == len(i):
                count+=1
    print(count)