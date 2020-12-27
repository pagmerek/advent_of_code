with open('input') as f:
    data = f.read().split(',')
    word_dict = {}
    for i in range(len(data)):
        word_dict[int(data[i])] = (i+1,i+1)
    i = len(data)+1
    last_word = 0
    while i < 30000000:
        if last_word in word_dict:
            temp = i - word_dict[last_word][1]
            word_dict[last_word] = (i,word_dict[last_word][0])
            if temp in word_dict:
                word_dict[temp] = (i+1,word_dict[temp][0])
            else:
                word_dict[temp] = (i+1,i+1)
            last_word=temp
        else:
            word_dict[last_word] = (i,i)
            last_word = 0
        i+=1
    print(last_word)


    