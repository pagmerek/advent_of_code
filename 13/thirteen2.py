def gcdExtended(a, b):  
    if a == 0 :   
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)  
    x = y1 - (b//a) * x1  
    y = x1  
    return gcd,x,y 

with open('input') as f:
    data = [x.strip() for x in f.readlines()]
    values = data[1].split(',')
    timestamp = int(values[0])
    mod = 1
    for i in range(0,len(values)):
        if(values[i]!='x'):
            second_mod = int(values[i])
            _, first_covariant, second_covariant = gcdExtended(mod,second_mod)
            timestamp = first_covariant*mod*(-i+second_mod) + second_covariant*second_mod*timestamp
            mod *= second_mod

    print(timestamp%mod)
