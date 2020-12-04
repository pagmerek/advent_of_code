
import math
import string  
def check(value):  
    for letter in value:  
        if letter not in string.hexdigits:  
            return False
    return True

with open('input') as f:
    data_table = f.readlines()
    data_table = [x.strip() for x in data_table]
    data_table.append('')
    check_table = [0,0,0,0,0,0,0]
    counter = 0
    for line in data_table:
        strings = line.split()
        print(strings)
        for i in strings:
            if i[:3]=='byr':
                if(len(i[4:])==4 and int(i[4:]) >= 1920 and int(i[4:])<=2002):
                    check_table[0] = 1
            if i[:3]=='iyr':
                if(len(i[4:])==4 and int(i[4:]) >= 2010 and int(i[4:])<=2020):
                    check_table[1] = 1
            if i[:3]=='eyr':
                 if(len(i[4:])==4 and int(i[4:]) >= 2020 and int(i[4:])<=2030):
                    check_table[2] = 1
            if i[:3]=='hgt':
                metric = i[-2:]
                if ((metric == 'cm' and (int(i[4:-2])>=150 and int(i[4:-2])<=193)) 
                or (metric =='in' and (int(i[4:-2])>=59 and int(i[4:-2])<=76))):
                    check_table[3] = 1
            if i[:3]=='hcl':
                if i[4] == '#' and check(i[5:]):
                    check_table[4] = 1
            if i[:3]=='ecl':
                if i[4:] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    check_table[5] = 1
            if i[:3]=='pid':
                if len(i[4:]) == 9:
                    check_table[6] = 1
        if(line == '' and math.prod(check_table) == 0):
             check_table = [0 for i in check_table]
        elif(line == '' and math.prod(check_table)!=0): 
            counter+=1
            check_table = [0 for i in check_table]
        print(check_table)
    print(counter)