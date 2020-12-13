with open('input') as f:
    data = [x.strip() for x in f.readlines()]
    num = int(data[0])
    values = data[1].split(',')
    print(num,values)
    i = 0
    curr = values[i]
    while True:
        if curr == 'x':
            i+=1
            curr = values[i]
        else:            
            if i == len(values)-1:
                i = 0
                num+=1       
            if int(num) % int(curr) == 0:
                print((int(num)-int(data[0]))*int(curr))
                break
            else:
                i+=1
                curr = values[i]
           
