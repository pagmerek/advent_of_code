with open('input') as f:
    current = 3
    horizontal = 0
    vertical = 0
    data = [x.strip() for x in f.readlines()]
    dirs = {0:'N', 1:'W', 2:'S', 3:'E'}
    for command in data:
        num = int(command[1:])
        char = command[0]
        if char == 'N':
            vertical+=num
        elif char == 'S':
            vertical -= num
        elif char == 'E':
            horizontal += num
        elif char == 'W':
            horizontal -= num
        elif char == 'L':
            num = num / 90
            current += num
            current = current % 4
        elif char == 'R':
            num = num / 90
            current -= num
            current = current % 4
        elif char == 'F':
            sec_char = dirs[current]
            if sec_char == 'N':
                vertical+=num
            elif sec_char == 'S':
                vertical -= num
            elif sec_char == 'E':
                horizontal += num
            elif sec_char == 'W':
                horizontal -= num
        print(horizontal,vertical)
    print(abs(horizontal)+abs(vertical))

