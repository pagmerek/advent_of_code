
if __name__ == "__main__":
    with open('input') as f:
        data = f.readlines()
        data = [x.strip() for x in data]
    result = 0
    for _, line in enumerate(data):
        line = line.split(' ')
        c_line = line.copy()
        paren = 0
        ind = [0]
        for i in range(len(c_line)):
            open_paren = line[i].count('(')
            closed_paren = line[i].count(')')
            paren += open_paren
            if open_paren > 0:
                for x in range(open_paren): 
                    ind.insert(0,i)
                    indx = i
            paren -= closed_paren
            if(closed_paren) > 0:
                for x in range(closed_paren):
                    indx = ind.pop(0)
            if len(ind)==0: ind.append(0)
            if(line[i]!='+' and line[i]!='*' and i != 0 and i != ind[0]):
                line[ind[0]] = '(' + line[ind[0]]
                line[i] += ')'
        print("".join(line))
        result += (eval("".join(line)))
    print(result)


