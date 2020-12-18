class Num:
    def __init__(self, a):
        self.a = a
    def __add__(self,i):
        return Num(self.a * i.a)
    def __mul__(self,i):
        return Num(self.a + i.a)
    def __str__(self): 
        return str(self.a)
if __name__ == "__main__":
    with open('input') as f:
        data = f.readlines()
        data = [x.strip() for x in data]
    result = Num(0)
    for _, line in enumerate(data):
        line = line.split(' ')
        for i, val in enumerate(line):
            if(val == '+'): line[i] = '*'
            elif(val == '*'): line[i] = '+'
            else:
                prefix = 0
                postfix = 0
                if val[0] == '(':
                    prefix = val.count('(')
                    line[i] = prefix*'(' + 'Num(' + "".join(line[i][prefix:]) +')'
                elif val[-1] == ')':
                    postfix = val.count(')')
                    line[i] = 'Num(' + "".join(line[i][:-postfix]) +')' + postfix*')'
                else:
                    line[i] = 'Num(' + line[i] +')'

                        
        result *= (eval("".join(line)))
    print(result)


