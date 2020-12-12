with open('input') as f:
    current = 3
    horizontal = 0
    vertical = 0
    w_horizontal = 10
    w_vertical = 1
    data = [x.strip() for x in f.readlines()]
    dirs = {0:'N', 1:'W', 2:'S', 3:'E'}
    for command in data:
        num = int(command[1:])
        char = command[0]
        if char == 'N':
            w_vertical+=num
        elif char == 'S':
            w_vertical -= num
        elif char == 'E':
            w_horizontal += num
        elif char == 'W':
            w_horizontal -= num
        elif char == 'L':
            num = num // 90
            for i in range(num):
                w_horizontal, w_vertical = -w_vertical, w_horizontal
        elif char == 'R':
            num = num // 90
            for i in range(num):
                w_horizontal, w_vertical = w_vertical, -w_horizontal
        elif char == 'F':
            sec_char = dirs[current]
            vertical += num*w_vertical
            horizontal += num*w_horizontal
        print(horizontal,vertical)
    print(abs(horizontal)+abs(vertical))

