with open('data.txt') as f:
    numbers = f.read()
    n = int(input())
    p = int(input())
    list1_del_n = []
    list2_pow_p = []
    text_list = numbers.split(sep=' ')
    i = 1
    for i in range(len(text_list)):
        if int(text_list[i]) % n == 0:
            list1_del_n.append(int(text_list[i]))
        list2_pow_p.append(int(text_list[i])**p)
        i += 1
    file1 = open('out-1.txt', 'w')
    file1.write(str(list1_del_n).replace(',', ' '))
    file2 = open('out-2.txt', 'w')
    file2.write(str(list2_pow_p).replace(',', ' '))
    file1.close()
    file2.close()

