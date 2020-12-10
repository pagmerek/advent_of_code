with open('input') as f:
    data = f.readlines()
    data = [int(x.strip()) for x in data]
    i = 0
    while i < len(data):
        k = i
        while k < len(data):
            sum_table = []
            number = 177777905              
            for j in range(i,k):
                sum_table.append(data[j])
                number -= data[j]
                if number == 0:
                    print(min(sum_table)+max(sum_table))
                    i=k=j=len(data)
                if number < 0: break
            k+=1
        i+=1
