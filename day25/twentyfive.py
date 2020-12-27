
def reverse_transform(target, number = 7):
    loop_size = 1
    value = 1
    while True:
        value *= number
        value = value % 20201227
        if value == target:
            break
        else:
            loop_size+=1
    return loop_size

if __name__ == '__main__':
    card_public_key = 15113849
    door_public_key = 4206373
    door_loop_size = reverse_transform(door_public_key)
    decryption_val = 1
    for _  in range(door_loop_size):
        decryption_val *= card_public_key
        decryption_val = decryption_val % 20201227
    print(decryption_val)
