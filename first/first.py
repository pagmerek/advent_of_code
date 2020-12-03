def second():
    with open('input') as f:
        read_data = f.read()
        read_table = read_data.split()
        for i in read_table:
            for j in read_table:
                for z in read_table:
                    if int(i)+int(z)+int(j) == 2020:
                        print(int(i)*int(z)*int(j))
if __name__ == "__main__":
    second()
    

